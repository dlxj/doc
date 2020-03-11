检查是否真的开启了 GPU（即当前连接到了GPU实例），可以直接在 Jupyter Notebook 中运行以下命令：

```python
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
 raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))
```

若输出以下语句，则表明已经使用了 GPU 实例。

> Found GPU at: /device: GPU: 0