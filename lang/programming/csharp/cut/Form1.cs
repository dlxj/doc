using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;

using MaterialSkin;
using MaterialSkin.Controls;


namespace MathpixCsharp
{
    public partial class Form1 : Form
    {
        //GetCode gg = new GetCode();
        //[System.Runtime.InteropServices.DllImport("user32.dll")]
        //private static extern bool RegisterHotKey(IntPtr hWnd, int id, int fsModifiers, int vk);
        Bitmap bit;
        public bool success;
        public bool cancelled;
        int last_choice = 3;
        string app_id = "";
        string app_key = "";

        public Bitmap Bit { get => bit; set => bit = value; }

        public Form1()
        {
            InitializeComponent();
            this.pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;


        }


        private void button1_Click(object sender, EventArgs e)
        {
            Clipboard.SetDataObject("set by C#.");
            string t = Clipboard.GetText(TextDataFormat.Text);
            

            ScreenShot sf = new ScreenShot();
            sf.Owner = this;
            this.Opacity = 0.0;
            this.success = false;
            this.cancelled = false;
            sf.ShowDialog();//make sure it's done
            if (this.cancelled)
            {
                this.Opacity = 1.0;
                return;
            }
            if (!this.success)
            {
                this.Opacity = 1.0;
                MessageBox.Show("错误，请重试");
                return;
            }

            this.pictureBox1.Image = Bit;
            Bit.Save("xxxxxxxxxxx.bmp");
            //ScreenShotToCode(Bit);
            this.Opacity = 1.0;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            GlobalHotKey.RegisterHotKey("Alt + Shift + S", () => {
                var a = 1;
            });

            //SystemHotKey.RegHotKey(this.Handle, 701, SystemHotKey.KeyModifiers.Alt | SystemHotKey.KeyModifiers.Ctrl | SystemHotKey.KeyModifiers.Shift, System.Windows.Forms.Keys.Back);
        }

        //protected override void WndProc(ref Message m)
        //{
        //    if ( m.Msg == WmHotKey)
        //    {
        //        var a = 1;
        //    }

        //    base.WndProc(ref m);
        //}
    }
}
