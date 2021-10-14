

using AntDesign;
using AntDesign.JsInterop;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;
using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Threading.Tasks;
using System.Timers;

namespace dangan.Client
{
    public partial class Index : AntDomComponentBase
    {
        private bool _isPlaying = false;
        private string PlayPauseIcon { get => _isPlaying ? "pause" : "caret-right"; }

        [Inject]
        private IDomEventListener DomEventListener { get; set; }

        protected override void OnInitialized()
        {
            base.OnInitialized();
        }

        protected override Task OnFirstAfterRenderAsync()
        {
            DomEventListener.AddEventListenerToFirstChild<JsonElement>("#audio", "play", OnPlay);

            return base.OnFirstAfterRenderAsync();
        }

        private void OnPlay(JsonElement jsonElement)
        {
            _isPlaying = true;
        }

        private async void OnPlayPause(MouseEventArgs args)
        {
            try
            {
                await JsInvokeAsync("Music.play", "#audio", !_isPlaying);

                _isPlaying = true;

                Refresh();
            }
            catch (Exception ex)
            {
            }
        }
    }
}