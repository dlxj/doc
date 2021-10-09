using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using Microsoft.Graph;


namespace dangan.Shared.lib
{
    public class BytesConverter : JsonConverter<byte[]>
    {
        public override byte[] Read(
        ref Utf8JsonReader reader,
        Type typeToConvert,
        JsonSerializerOptions options)
        {
            string ret = reader.GetString(); //?.ConvertToBinary();

            Encoding utf8 = Encoding.UTF8;
            return utf8.GetBytes(ret);
        }

        public override void Write(
        Utf8JsonWriter writer,
        byte[] value, JsonSerializerOptions options)
        {
            writer.WriteStartArray();
            foreach (var val in value)
            {
                writer.WriteNumberValue(val);
            }
            writer.WriteEndArray();
        }
    }

    /// <summary>
    /// serialize an object to JSON
    /// </summary>
    public class Serializer //: ISerializer
    {
        private static readonly JsonSerializerOptions Options = new JsonSerializerOptions();

        static Serializer()
        {
            Options.Converters.Add(new BytesConverter());
        }

        public string Serialize(object obj)
        {
            return JsonSerializer.Serialize(obj, Options);
        }

        public Task SerializeAsync<T>(T obj, Stream stream)
        {
            return JsonSerializer.SerializeAsync<T>(stream, obj, Options);
        }

        public object DeSerialize(string input, Type targetType)
        {
            return JsonSerializer.Deserialize(input, targetType, Options);
        }
    }
}
