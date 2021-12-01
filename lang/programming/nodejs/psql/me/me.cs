

using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}


// using MeCab;

// public static string mecab(string sentence)
// {
//     string result = "";

//     var parameter = new MeCabParam();
//     var tagger = MeCabTagger.Create(parameter);

//     foreach (var node in tagger.ParseToNodes(sentence))
//     {
//         if (node.CharType > 0)
//         {
//             var features = node.Feature.Split(',');
//             var displayFeatures = string.Join(", ", features);

//             result += $"{node.Surface}\t{displayFeatures}\n";
//         }
//     }

//     return result;
// }

