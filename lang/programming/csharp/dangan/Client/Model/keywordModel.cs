using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using System.ComponentModel.DataAnnotations;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace dangan.Client.Model
{
    public class KeywordModel
    {
        [Required]
        [StringLength(30, ErrorMessage = "keyword is too long.")]
        public string keyword { get; set; }
    }

    public class rowModel
    {
        [JsonPropertyName("id")]
        public string id { get; set; }

        [JsonPropertyName("jp")]
        public string jp { get; set; }

        [JsonPropertyName("zh")]
        public string zh { get; set; }


        [JsonPropertyName("time")]
        public string time { get; set; }
    }
}
