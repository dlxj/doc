

# cudatoolkit

```
see nodejs summary.md -> InternLM -> Ubuntu22.04

disable secure boot in bios
apt install --reinstall linux-headers-$(uname -r)

关闭安全启动 nvidia 驱动就正常加载了。

nvidia-smi

disable secure boot

The target kernel has CONFIG_MODULE_SIG set
UEFI Secure Boot enabled

disable secure boot in bios
apt install --reinstall linux-headers-$(uname -r)


wget https://us.download.nvidia.com/XFree86/Linux-x86_64/535.113.01/NVIDIA-Linux-x86_64-535.113.01.run
	# 下载驱动

 # sh ./NVIDIA-Linux-x86_64-535.113.01.run -s \
--module-signing-secret-key=/usr/share/nvidia/nvidia-modsign-key-C4BF4B44.key \
--module-signing-public-key=/usr/share/nvidia/nvidia-modsign-crt-C4BF4B44.der

Unable to determine the path to install the libglvnd EGL vendor library    
           config files. Check that you have pkg-config and the libglvnd development  
           libraries installed, or specify a path with --glvnd-egl-config-path.

nvidia-smi

NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.

ls /usr/src | grep nvidia
	nvidia-535.113.01

apt install dkms
dkms install -m nvidia -v 535.113.01
	# 安全启动密码是: rootroot
	
dpkg --get-selections | grep linux-image
	linux-image-5.15.0-86-generic                   install
	linux-image-generic                             install
	# 查看已安装内核
	
uname -a
	# 查看正在使用的内核
	
ll /usr/src



wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
	# 下载 cuda toolkit


sh cuda_11.8.0_520.61.05_linux.run
	# /usr/local/cuda-11.8/bin
	# /usr/local/cuda-11.8/lib64

echo 'export PATH=/usr/local/cuda-11.8/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
sudo ldconfig

nvcc
nvidia-smi
```





# how-to-optim-algorithm-in-cuda

[how-to-optim-algorithm-in-cuda](https://github.com/BBuf/how-to-optim-algorithm-in-cuda)



# μ-CUDA

[μ-CUDA](https://zhuanlan.zhihu.com/p/592439225)

