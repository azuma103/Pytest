# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from objc_util import NSBundle, ObjCClass
import twitter, ui, dialogs, console

def tweet(text):
    all_accounts = twitter.get_all_accounts()
    if len(all_accounts) >= 1:
        account = all_accounts[0] # get main account
        text = dialogs.text_dialog(text=text, autocapitalization=ui.AUTOCAPITALIZE_SENTENCES)
        if text:
            twitter.post_tweet(account, text, parameters=None)
            console.hud_alert('Tweet Posted!', 'success', 1.5)
        else:
            console.hud_alert('Canceled', 'error', 1.5)

if __name__ == '__main__':
    NSBundle.bundleWithPath_('/System/Library/Frameworks/MediaPlayer.framework').load()
    MPMusicPlayerController = ObjCClass('MPMusicPlayerController')
    ipod_player = MPMusicPlayerController.iPodMusicPlayer()
    now_playing = ipod_player.nowPlayingItem()
    if now_playing:
        artist = now_playing.valueForProperty_('artist')
        title = now_playing.valueForProperty_('title')
        album = now_playing.valueForProperty_('albumTitle')
        text = '#Nowplaying {0} - {1}({2})'.format(artist, title, album)
        tweet(text)
    else:
        print('No music playing')
