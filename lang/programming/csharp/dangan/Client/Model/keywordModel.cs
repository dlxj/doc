using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using System.ComponentModel.DataAnnotations;


namespace dangan.Client.Model
{
    public class KeywordModel
    {
        [Required]
        [StringLength(30, ErrorMessage = "keyword is too long.")]
        public string keyword { get; set; }
    }
}
