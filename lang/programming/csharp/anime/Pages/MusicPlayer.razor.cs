
// https://zhuanlan.zhihu.com/p/157582707 GetMusicTime



using AntDesign;
using AntDesign.JsInterop;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;
using OneOf;
using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Threading.Tasks;
using System.Timers;


namespace anime.music
{

    public partial class MusicPlayer : AntDomComponentBase
    {
        private bool _isPlaying = false;
        private bool _canPlayFlag = false;
        private string _currentSrc;
        private List<string> _musicList = new List<string>
        {
            "music/01.mp3",
        };
        private Timer _timer;
        private double _currentTimeSlide = 0;
        private TimeSpan _currentTime = new TimeSpan(0);
        private TimeSpan _duration = new TimeSpan(0);
        private string PlayPauseIcon { get => _isPlaying ? "pause" : "caret-right"; }
        private Action _afterCanPlay;
        [Inject]
        private IDomEventListener DomEventListener { get; set; }

        protected override void OnInitialized()
        {
            base.OnInitialized();

            _currentSrc = _musicList[0];
            //_afterCanPlay = async () =>
            //{
            //    // do not use _isPlaying, this delegate will be triggered when user clicked play button
            //    if (_canPlayFlag)
            //    {
            //        try
            //        {
            //            await JsInvokeAsync("Music.play", "#audio", true);
            //            _canPlayFlag = false;
            //        }
            //        catch (Exception ex)
            //        {
            //        }
            //    }
            //};
        }

        protected override Task OnFirstAfterRenderAsync()
        {


            // cannot listen to dom events in OnInitialized while render-mode is ServerPrerendered
            //DomEventListener.AddEventListenerToFirstChild<JsonElement>("#audio", "timeupdate", OnTimeUpdate);
            //DomEventListener.AddEventListenerToFirstChild<JsonElement>("#audio", "canplay", OnCanPlay);
            DomEventListener.AddEventListenerToFirstChild<JsonElement>("#audio", "play", OnPlay);
            //DomEventListener.AddEventListenerToFirstChild<JsonElement>("#audio", "pause", OnPause);
            //DomEventListener.AddEventListenerToFirstChild<JsonElement>("#audio", "ended", OnEnd);
            return base.OnFirstAfterRenderAsync();
        }

        #region Audio EventHandlers

        private async void OnPlayPause(MouseEventArgs args)
        {
            try
            {
                await JsInvokeAsync("Music.play", "#audio", !_isPlaying);
            }
            catch (Exception ex)
            {
            }
        }

        private async void OnCanPlay(JsonElement jsonElement)
        {
            try
            {
                string json = await JsInvokeAsync<string>("Music.getMusicTime", "#audio");
                jsonElement = JsonDocument.Parse(json).RootElement;
                _duration = TimeSpan.FromSeconds(jsonElement.GetProperty("duration").GetDouble());

                _afterCanPlay();
            }
            catch (Exception)
            {
            }
        }

        private void OnPlay(JsonElement jsonElement)
        {
            _isPlaying = true;
        }

        private async void OnLast(MouseEventArgs args)
        {
            _canPlayFlag = true;
            int index = _musicList.IndexOf(_currentSrc);
            index = index == 0 ? _musicList.Count - 1 : index - 1;
            _currentSrc = _musicList[index];
        }

        private async void OnNext(MouseEventArgs args)
        {
            _canPlayFlag = true;
            int index = _musicList.IndexOf(_currentSrc);
            index = index == _musicList.Count - 1 ? 0 : index + 1;
            _currentSrc = _musicList[index];
        }

        private void OnPause(JsonElement jsonElement)
        {
            _isPlaying = false;
            StateHasChanged();
        }

        private void OnEnd(JsonElement jsonElement)
        {
            _isPlaying = false;
            StateHasChanged();

            OnNext(new MouseEventArgs());
        }

        private async void OnTimeUpdate(JsonElement jsonElement)
        {
            // do not use the timestamp from timeupdate event, which is the total time the audio has been working
            // use the currentTime property from audio element
            string json = await JsInvokeAsync<string>("Music.getMusicTime", "#audio");
            jsonElement = JsonDocument.Parse(json).RootElement;
            _currentTime = TimeSpan.FromSeconds(jsonElement.GetProperty("currentTime").GetDouble());
            _currentTimeSlide = _currentTime / _duration * 100;

            StateHasChanged();
        }

        #endregion

        private async void OnSliderChange(double value) // OneOf<double, (double, double)>
        {
            //_currentTime = value.AsT0 * _duration / 100;
            _currentTime = value * _duration / 100;
            _currentTimeSlide = _currentTime / _duration * 100;
            await JsInvokeAsync("Music.setMusicTime", "#audio", _currentTime.TotalSeconds);
        }
    }
}
