using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Net;
using System.Net.Security;
using System.Net.Sockets;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading;
using System.Web;

public delegate void postBefore(System.Net.HttpWebRequest request, Dictionary<string, object> headers);
public delegate void postCallBack(HttpWebRequest request, HttpWebResponse response);


public class HttpTools
{


    public HttpTools()
    {

    }


    public static void openSSL()
    {
        ServicePointManager.DefaultConnectionLimit = 3000;
        ServicePointManager.ServerCertificateValidationCallback = new RemoteCertificateValidationCallback(CheckValidationResult);
    }




    static System.Threading.Semaphore sem = new System.Threading.Semaphore(1, 1);

    /// <summary>
    /// 发起带cookie的post请求
    /// </summary>
    /// <param name="url">URL</param>
    /// <param name="param">参数name=value&name=value</param>
    /// <param name="cookie">cookie</param>
    /// <returns></returns>
    public static string PostMoths(string url, string param, CookieContainer cookie, string referer = "", WebProxy wp = null, string XRequestedWith = "", string CacheControl = "", string accept = "")
    {
        string strValue = "";
        try
        {
            //if (webProxy != null)
            //{
            //    wp = webProxy;
            //}
            //wp = new WebProxy("xxx.xxx.xxx.xxx", port);
            string strURL = url;
            System.Net.HttpWebRequest request;
            request = (System.Net.HttpWebRequest)WebRequest.Create(strURL);
            request.Timeout = 100000;
            //允许最大连接数  
            System.Net.ServicePointManager.DefaultConnectionLimit = 1024;
            request.ServicePoint.ConnectionLimit = 1024;
            request.AllowWriteStreamBuffering = false;
            request.KeepAlive = true;
            request.CookieContainer = cookie;
            request.ServicePoint.Expect100Continue = false;
            // ServicePointManager.ServerCertificateValidationCallback = new RemoteCertificateValidationCallback(CheckValidationResult);


            request.Accept = (accept == "" || accept == null) ? "image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*" : accept;
            request.Headers.Add("Accept-Language", "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3");
            request.Headers.Add("UA-CPU", "AMD64");
            request.Headers.Add("Accept-Encoding", "gzip, deflate");
            request.UserAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36";

            if (XRequestedWith != null && XRequestedWith != "")
            {
                request.Headers.Add("X-Requested-With", XRequestedWith);
            }

            if (CacheControl != null && CacheControl != "")
            {
                request.Headers.Add("Cache-Control", CacheControl);
            }

            request.Method = "POST";
            request.ContentType = "application/x-www-form-urlencoded;charset=UTF-8";
            request.Proxy = null;
            if (referer != "" && referer != null)
            {
                request.Referer = referer;
            }
            if (wp != null)
            {
                request.Proxy = wp;
            }

            string paraUrlCoded = param;
            byte[] payload;
            payload = System.Text.Encoding.UTF8.GetBytes(paraUrlCoded);
            request.ContentLength = payload.Length;
            Stream writer = request.GetRequestStream();
            writer.Write(payload, 0, payload.Length);
            //writer.Close();
            System.Net.HttpWebResponse response;
            response = (System.Net.HttpWebResponse)request.GetResponse();
            System.IO.Stream s;
            s = response.GetResponseStream();

            //cookie.Add(response.Cookies);

            string contentType = response.Headers["content-type"];

            Encoding enco = Encoding.UTF8;


            string StrDate = "";

            StreamReader Reader = new StreamReader(s, enco);
            //while ((StrDate = Reader.ReadLine()) != null)
            //{
            //    strValue += StrDate + "\r\n";
            //}
            strValue = Reader.ReadToEnd();
            //s.Close();
            //s.Dispose();
            //response.Close();

        }
        catch (Exception ex)
        {
            Console.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + "：HTTP POST 异常：" + ex.Message + "|" + ex.StackTrace + "|" + url);
        }
        //s.Close();
        //s.Dispose();
        //response.Close();
        return strValue;
    }


    private static bool CheckValidationResult(object sender, X509Certificate certificate, X509Chain chain, SslPolicyErrors errors)
    {
        return true;
    }
}