using System;
using System.Runtime.InteropServices;
using System.Threading;
using System.Windows.Forms;

namespace MathpixCsharp
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public class HotKey
    {
        public enum ModifierKeys { None = 0, Alt = 1, Ctrl = 2, Shift = 4, Windows = 8 }

        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool RegisterHotKey(IntPtr hWnd, int id, ModifierKeys fsModifiers, Keys vk);

        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool UnregisterHotKey(IntPtr hWnd, int id);

        [DllImport("user32")]
        private static extern int ToAscii(int uVirtKey, int uScanCode, byte[] lpbKeyState, byte[] lpwTransKey, int fuState);

        [DllImport("user32")]
        internal static extern int GetKeyboardState(byte[] pbKeyState);

        [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
        private static extern short GetKeyState(int vKey);

        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr SetWindowsHookEx(int idHook, LowLevelKeyboardProc lpfn, IntPtr hMod, uint dwThreadId);

        [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr GetModuleHandle(string lpModuleName);


        private static int _lastHotKeyId = 0;
        private readonly int _id;

        public bool IsRegistered;

        private byte[] _keyboardStateNative;

        public delegate void HotKeyPressedEventHandler(object sender, EventArgs e);

        public event HotKeyPressedEventHandler HotKeyPressed;

        public const int WmHotKey = 786;

        private IntPtr _hookId = IntPtr.Zero;

        private delegate IntPtr LowLevelKeyboardProc(int nCode, IntPtr wParam, IntPtr lParam);
        private LowLevelKeyboardProc _proc;

        private const int WH_KEYBOARD_LL = 13;

        private const int WM_KEYDOWN = 0x100;
        private const int WM_KEYUP = 0x101;
        private const int WM_SYSKEYDOWN = 0x104;
        private const int WM_SYSKEYUP = 0x105;

        private const byte VK_SHIFT = 0x10;
        private const byte VK_CAPITAL = 0x14;

        public event System.Windows.Forms.KeyEventHandler KeyDown;
        public event System.Windows.Forms.KeyPressEventHandler KeyPress;
        public event System.Windows.Forms.KeyEventHandler KeyUp;

        [StructLayout(LayoutKind.Sequential)]
        private sealed class KeyboardHookStruct
        {
            /// <summary>
            /// Specifies a virtual-key code. The code must be a value in the range 1 to 254. 
            /// </summary>
            public int vkCode;
            /// <summary>
            /// Specifies a hardware scan code for the key. 
            /// </summary>
            public int scanCode;
            /// <summary>
            /// Specifies the extended-key flag, event-injected flag, context code, and transition-state flag.
            /// </summary>
            public int flags;
            /// <summary>
            /// Specifies the time stamp for this message.
            /// </summary>
            public int time;
            /// <summary>
            /// Specifies extra information associated with the message. 
            /// </summary>
            public int dwExtraInfo;
        }

        public void SendToLeft()
        {

        }

        private void SendToLeft(object sender, EventArgs eventArgs) => SendToLeft();

        private byte MyGetKeyState(Keys key)
        {
            var virtualKeyCode = (int)key;
            if (virtualKeyCode < 0 || virtualKeyCode > 255)
            {
                throw new ArgumentOutOfRangeException(nameof(key), key, "The value must be between 0 and 255.");
            }
            return _keyboardStateNative[virtualKeyCode];
        }

        private static bool GetHighBit(byte value)
        {
            return (value >> 7) != 0;
        }

        private static bool GetLowBit(byte value)
        {
            return (value & 1) != 0;
        }

        public bool IsDown(Keys key)
        {
            var keyState = MyGetKeyState(key);
            var isDown = GetHighBit(keyState);
            return isDown;
        }

        //private void ThreadPreprocessMessageMethod(ref MSG msg, ref bool handled)
        //{
        //    if (handled || msg.message != WmHotKey || (int)msg.wParam != _id)
        //        return;

        //    // hot key pressed

        //    // List pressed keys
        //    //var keys = new List<Keys>();
        //    //var keyboardStateNative = new byte[256];
        //    //GetKeyboardState(keyboardStateNative);
        //    //_keyboardStateNative = keyboardStateNative;

        //    //for (var i = 0; i < 256; i++)
        //    //{
        //    //    if (IsDown((Keys)i))
        //    //    {
        //    //        keys.Add((Keys)i);
        //    //    }
        //    //}

        //    /*

        //    if (!keys.Contains(e.KeyData))
        //    {
        //        keys.Add(e.KeyData);
        //    }

        //    // Find hotkey
        //    foreach (HotKey hotKey in _hotKeys)
        //    {
        //        if (hotKey.Equals(keys))
        //        {
        //            if (hotKey.Action != null)
        //            {
        //                hotKey.Action(sender, EventArgs.Empty);
        //                e.Handled = true;
        //            }
        //        }
        //    }
        //    */

        //    int a = 1;

        //    //OnHotKeyPressed();
        //    //handled = true;
        //}

        private IntPtr HookCallback(int nCode, IntPtr wParam, IntPtr lParam)
        {
            var handled = false;
            if (nCode >= 0)
            {
                var myKeyboardHookStruct = (KeyboardHookStruct)Marshal.PtrToStructure(lParam, typeof(KeyboardHookStruct));
                if ((wParam.ToInt32() == WM_KEYDOWN || wParam.ToInt32() == WM_SYSKEYDOWN))
                {
                    var keyData = (Keys)myKeyboardHookStruct.vkCode;
                    var e = new System.Windows.Forms.KeyEventArgs(keyData);

                    //ctrl+alt+上下调整水平线
                    if (e.Shift && e.Alt && (e.KeyValue == 38 || e.KeyValue == 40))
                    {
                        //lineY = e.KeyValue == 38 ? lineY - 2 : lineY + 2;
                        //this.line1.Top = lineY + 10;

                        int a = 0;
                    }

                    //KeyDown(this, e);
                    handled = handled || e.Handled;
                }

                if (wParam.ToInt32() == WM_KEYDOWN)
                {
                    var isDownShift = (GetKeyState(VK_SHIFT) & 0x80) == 0x80;
                    var isDownCapslock = GetKeyState(VK_CAPITAL) != 0;

                    var keyState = new byte[256];
                    GetKeyboardState(keyState);
                    var inBuffer = new byte[2];
                    if (ToAscii(myKeyboardHookStruct.vkCode, myKeyboardHookStruct.scanCode, keyState, inBuffer, myKeyboardHookStruct.flags) == 1)
                    {
                        var key = (char)inBuffer[0];
                        if ((isDownCapslock ^ isDownShift) && char.IsLetter(key)) key = char.ToUpperInvariant(key);
                        var e = new KeyPressEventArgs(key);
                        //KeyPress(this, e);
                        handled = handled || e.Handled;
                    }
                }

                if ((wParam.ToInt32() == WM_KEYUP || wParam.ToInt32() == WM_SYSKEYUP))
                {
                    var keyData = (Keys)myKeyboardHookStruct.vkCode;
                    var e = new System.Windows.Forms.KeyEventArgs(keyData);
                    //KeyUp(this, e);
                    handled = handled || e.Handled;
                }
            }

            // if event handled in application do not handoff to other listeners
            return new IntPtr(1);
        }

        void HookKeyDown(object sender, System.Windows.Forms.KeyEventArgs e)
        {

        }

        public HotKey()
        {

            ModifierKeys fsModifiers = ModifierKeys.Windows;
            Keys vk = Keys.NumPad7;
            _id = Interlocked.Increment(ref _lastHotKeyId);
            IntPtr hWnd = (IntPtr)0x0; //new WindowInteropHelper(System.Windows.Application.Current.MainWindow).Handle;

            //ComponentDispatcher.ThreadPreprocessMessage += ThreadPreprocessMessageMethod;
            // ThreadPreprocessMessageMethod 
            // 内部维护一个 _id ，win32 函数 RegisterHotKey 注册热键时把这个 _id 传进去。只要有热键触发就会回调 ThreadPreprocessMessageMethod，参数 msg.wParam 如果等于 _id 就表明你注删的热键触发了


            IsRegistered = RegisterHotKey(hWnd, _id, fsModifiers, vk);

            //_proc = HookCallback;
            //var curProcess = Process.GetCurrentProcess();
            //ProcessModule curModule = curProcess.MainModule;
            //_hookId = SetWindowsHookEx(WH_KEYBOARD_LL, _proc, GetModuleHandle(curModule.ModuleName), 0);



            //KeyDown += new System.Windows.Forms.KeyEventHandler(HookKeyDown);

            //HotKeyPressed += SendToLeft;

            //ComponentDispatcher.ThreadPreprocessMessage += ThreadPreprocessMessageMethod;

            //IsRegistered = !UnregisterHotKey(hWnd, _id);

        }

        ///// 监视Windows消息
        ///// 重载WndProc方法，用于实现热键响应
        //protected override void WndProc(ref Message m)
        //{
        //    const int WM_HOTKEY = 0x0312;
        //    //按快捷键 
        //    switch (m.Msg)
        //    {
        //        case WM_HOTKEY:
        //            switch (m.WParam.ToInt32())
        //            {
        //                case 100:  //按下的是Shift+S
        //                           //此处填写快捷键响应代码     
        //                    MessageBox.Show("WndProc Shift+S");
        //                    break;
        //                case 101:  //按下的是Ctrl+C
        //                           //此处填写快捷键响应代码
        //                    MessageBox.Show("WndProc Ctrl+C");
        //                    break;
        //                case 102:  //按下的是Alt+D
        //                           //此处填写快捷键响应代码
        //                    MessageBox.Show("WndProc Alt+D");
        //                    break;
        //            }
        //            break;
        //    }
        //    base.WndProc(ref m);
        //}

    }
}
