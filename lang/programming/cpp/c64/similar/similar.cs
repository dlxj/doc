using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("sim.dll")]
        public static extern double sim(byte[] s1, byte[] s2);

        static Encoding GBKEndoding()
        {
            return Encoding.GetEncoding("gb18030");
        }

        static Encoding Utf8Endoding()
        {
            return Encoding.GetEncoding("utf-8");
        }

        static string gbk2utf8(string s) {
            return Utf8Endoding().GetString(Encoding.Convert(GBKEndoding(), Utf8Endoding(), GBKEndoding().GetBytes(s)));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 回家吃饭
            string s1 = textBox1.Text;
            string s2 = textBox2.Text;
            if (s1.Length == 0 || s2.Length == 0) {
                MessageBox.Show("请输入字符串！");
                return;
            }
            s1 = gbk2utf8(s1);
            s2 = gbk2utf8(s2);

            double similar = sim(Encoding.UTF8.GetBytes(s1), Encoding.UTF8.GetBytes(s2));

            MessageBox.Show("相似度：" + similar.ToString());
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }
    }
}
