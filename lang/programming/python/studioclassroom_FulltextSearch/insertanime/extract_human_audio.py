# https://github.com/YaoFANGUK/video-subtitle-extractor/issues/15
# https://gitee.com/m986883511/python_demo/blob/master/%E5%AD%97%E5%B9%95%E7%A1%AC%E6%8F%90%E5%8F%96/main.py
# marsmarcin
# 2020.3.11
# a test version for a beautiful system
# https://zmister.com/archives/477.html
import os
import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtCore import QThread, QProcess, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTextEdit, QLabel, QFileDialog, QMessageBox
from pydub import AudioSegment
from pydub.silence import split_on_silence
from subtext.scripts import get_extract_voice_progress

current_dir = os.path.dirname(__file__)


class MyThread(QThread):  # 线程2
    my_signal = pyqtSignal(int)
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.estimate_time = None
        self.finished = None
        self.input_func = None
        self.input_args = None
        self.input_kwargs = None
        self.result = None
        self.name = None

    def __fake_progress(self):
        start_time = time.perf_counter()
        while not self.finished:
            use_time = time.perf_counter() - start_time
            progress = int(100.0 * use_time / self.estimate_time)
            if progress > 95:
                progress = 95
            self.my_signal.emit(progress)
            time.sleep(0.25)
        self.log_signal.emit('假进度线程结束')

    def set_function(self, name, estimate_time, func, *args, **kwargs):
        self.name = name
        self.input_func = func
        self.estimate_time = estimate_time
        self.input_args = args
        self.input_kwargs = kwargs

    def run(self):
        if not callable(self.input_func):
            return
        self.log_signal.emit('{} thread start'.format(self.name))
        self.finished = False
        fake_thread = Thread(target=self.__fake_progress)
        fake_thread.setDaemon(True)
        fake_thread.start()
        self.result = self.input_func(*self.input_args, **self.input_kwargs)
        self.finished = True
        self.my_signal.emit(100)
        print(self.result)
        self.log_signal.emit('{} thread end'.format(self.name))


class MainUi(QtWidgets.QMainWindow):
    process = QProcess()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.video_file_path = ''
        self.output_voice_path = os.path.abspath(os.path.join(current_dir, 'temp', 'extract.mp3'))
        self.temp_path = os.path.abspath(os.path.join(current_dir, 'temp'))
        self.human_voice_file = os.path.abspath(os.path.join(self.temp_path, 'extract', 'vocals.wav'))
        self.voice_path = os.path.abspath(os.path.join(self.temp_path, 'voice'))
        self.prepare_dir()
        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.update_process_bar)
        self.my_thread.log_signal.connect(self.add_string_text)

    def prepare_dir(self):
        os.makedirs(os.path.join(current_dir, 'temp', 'voice'), exist_ok=True)
        os.makedirs(os.path.join(current_dir, 'temp', 'picture'), exist_ok=True)

    def init_ui(self):
        self.setFixedSize(1024, 600)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.up_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.up_widget.setObjectName('up_widget')
        self.up_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.up_widget.setLayout(self.up_layout)  # 设置左侧部件布局为网格
        self.process_bar = QtWidgets.QProgressBar()  # 播放进度部件
        self.process_bar.setValue(10)
        self.process_bar.setFixedHeight(5)  # 设置进度条高度
        self.process_bar.setTextVisible(False)  # 不显示进度条文字
        self.up_layout.addWidget(self.process_bar)
        self.main_layout.addWidget(self.up_widget, 0, 0, 1, 12)  # 左侧部件在第0行第0列，占12行2列

        self.zhong_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.zhong_widget.setObjectName('zhong_widget')
        self.zhong_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.zhong_widget.setLayout(self.zhong_layout)  # 设置左侧部件布局为网格
        self.show_text = QTextEdit()
        self.picture_label = QLabel("123123")
        self.zhong_layout.addWidget(self.show_text, 0, 6, 6, 6)
        self.zhong_layout.addWidget(self.picture_label, 0, 0, 6, 6)
        self.main_layout.addWidget(self.zhong_widget, 2, 0, 2, 12)  # 左侧部件在第0行第0列，占12行2列

        self.buttom_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.buttom_widget.setObjectName('zhong_widget')
        self.buttom_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.buttom_widget.setLayout(self.buttom_layout)  # 设置左侧部件布局为网格
        self.vedio_file_button = QtWidgets.QPushButton('选择视频文件')
        self.vedio_file_button.clicked.connect(self.get_video_file)  # 关联
        self.get_voice_button = QtWidgets.QPushButton('提取人声')
        self.get_voice_button.clicked.connect(self.get_video_voice)  # 关联
        self.split_voice_button = QtWidgets.QPushButton('计算字幕位置')
        self.split_voice_button.clicked.connect(self.split_human_voice)  # 关联

        self.get_subtext_button = QtWidgets.QPushButton('识别字幕')
        self.get_subtext_button.clicked.connect(self.split_human_voice_to_list)  # 关联

        self.buttom_layout.addWidget(self.vedio_file_button, 0, 0, 2, 3)
        self.buttom_layout.addWidget(self.get_voice_button, 0, 3, 2, 3)
        self.buttom_layout.addWidget(self.split_voice_button, 0, 6, 2, 3)
        self.buttom_layout.addWidget(self.get_subtext_button, 0, 9, 2, 3)
        self.main_layout.addWidget(self.buttom_widget, 10, 0, 2, 12)  # 左侧部件在第0行第0列，占12行2列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.main_layout.setSpacing(0)

        self.process.finished.connect(self.process_finishend)
        self.process.readyReadStandardError.connect(self.update_stderr)
        self.process.readyReadStandardOutput.connect(self.update_stdout)

    # 无边框的拖动
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())

    def split_human_voice(self):
        cmd = 'spleeter separate -d 1800 -p spleeter:2stems -o {} {}'.format(self.temp_path, self.output_voice_path)
        cmd_list = cmd.split(' ')
        self.process.start(cmd_list[0], cmd_list[1:])

    def update_process_bar(self, progress):
        self.process_bar.setValue(progress)

    def __deal_with_process_output_string(self, input_str):
        str1 = bytearray(input_str)
        str1 = str1.decode('gbk').strip()
        if str1:
            self.show_text.append(str1)
            progress = get_extract_voice_progress(str1)
            if progress:
                self.update_process_bar(progress)

    def update_stderr(self):
        str1 = self.process.readAllStandardError()
        self.__deal_with_process_output_string(str1)

    def update_stdout(self):
        str1 = self.process.readAllStandardOutput()
        self.__deal_with_process_output_string(str1)

    def add_string_text(self,str1):
        self.show_text.append(str1)


    def process_finishend(self, exitCode, exitStatus):
        if exitCode != 0:
            self.show_text.append('Abnormal End, exitCode={}, existStatus={}'.format(exitCode, exitStatus))
            QMessageBox.critical(self, 'command exception', 'process existed abnormally',
                                 QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.show_text.append('Normal End, exitCode={}, existStatus={}'.format(exitCode, exitStatus))

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def get_video_file(self):
        self.video_file_path = QFileDialog.getOpenFileName(self, '选择文件')[0]
        print(self.video_file_path)

    def get_video_voice(self):
        cmd = "ffmpeg -i {} {} -y".format(self.video_file_path, self.output_voice_path)
        cmd_list = cmd.split(' ')
        self.process.start(cmd_list[0], cmd_list[1:])

    def split_human_voice_to_list(self):
        def func():
            sound = AudioSegment.from_mp3(self.human_voice_file)
            chunks = split_on_silence(sound, min_silence_len=430,
                                      silence_thresh=-45, keep_silence=400)
            return chunks

        self.my_thread.set_function(name='根据声调分割语音', estimate_time=60, func=func)
        self.my_thread.start()

    # 关闭按钮动作函数
    def close_window(self):
        self.close()


def main():
    import cgitb

    cgitb.enable()
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()