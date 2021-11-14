
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

// 命令行运行方法：
// encodeconvert { big52gbk | WestEuropeanLatin2utf8 } fnamein fnameout
namespace EncodeConvert
{ 
    class Program {
		
		static void usage() {
			System.Console.WriteLine("argument: { big52gbk | WestEuropeanLatin2utf8 }	srcfname	desfname");
		}
		
        static void Main(string[] args) {
			if (args.Length != 3) {
				usage();
				return;
			}
			string op = args[0].ToString();
			string srcPath = args[1];
			string desPath = args[2];
			
			op = "WestEuropeanLatin2utf8";
 			
			switch (op) {
	    		case "big52gbk":
					big52gbk(srcPath, desPath);
					break;
	    		case "WestEuropeanLatin2utf8":
					WestEuropeanLatin2utf8(srcPath, desPath);
					break;
	    		default:
					usage();
					throw new Exception("bad argument");
			}
        }
        // 将gbk 编码的文件转换成utf8 编码的文件
        // 参数1：srcPath 要转换的文件路径
        // 参数2：desPath 目标文件路径
        static void big52gbk(string srcPath, string desPath) {
            string big5 = File.ReadAllText(srcPath, Big5Endoding());
            string utf8 = Utf8Endoding().GetString(Encoding.Convert(Big5Endoding(), Utf8Endoding(), Big5Endoding().GetBytes(big5)));
            File.WriteAllText(desPath, utf8, Utf8Endoding());
        }
		
		static void WestEuropeanLatin2utf8(string srcPath, string desPath) {
            string Latin = File.ReadAllText(srcPath, WestEuropeanLatinEndoding());
            string utf8 = Utf8Endoding().GetString(Encoding.Convert(WestEuropeanLatinEndoding(), Utf8Endoding(), 
			              	WestEuropeanLatinEndoding().GetBytes(Latin)));
            File.WriteAllText(desPath, utf8, Utf8Endoding());
        }

        static Encoding GBKEndoding() {
            return Encoding.GetEncoding("gb18030");
        }

        static Encoding Big5Endoding() {
            return Encoding.GetEncoding("big5");
        }

        static Encoding Utf8Endoding() {
			return new UTF8Encoding(false);  // NO Bom
        }
		
		static Encoding WestEuropeanLatinEndoding() {
			return Encoding.GetEncoding (1252);
		} 
			
    }
}