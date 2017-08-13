# /bin/sh

YOUR_API_KEY=YOUR_API_KEY

curl "https://api.voicetext.jp/v1/tts"   -u "${YOUR_API_KEY}:"   -d "text=おはよう"   -d "speaker=haruka"   -d "format=ogg"   -o voiceA.ogg
curl "https://api.voicetext.jp/v1/tts"   -u "${YOUR_API_KEY}:"   -d "text=こんにちは"   -d "speaker=haruka"   -d "format=ogg"   -o voiceB.ogg
curl "https://api.voicetext.jp/v1/tts"   -u "${YOUR_API_KEY}:"   -d "text=こんばんは"   -d "speaker=haruka"   -d "format=ogg"   -o voiceC.ogg
curl "https://api.voicetext.jp/v1/tts"   -u "${YOUR_API_KEY}:"   -d "text=おやすみ"   -d "speaker=haruka"   -d "format=ogg"   -o voiceD.ogg
curl "https://api.voicetext.jp/v1/tts"   -u "${YOUR_API_KEY}:"   -d "text=いってらっしゃい"   -d "speaker=haruka"   -d "format=ogg"   -o voiceBack.ogg
curl "https://api.voicetext.jp/v1/tts"   -u "${YOUR_API_KEY}:"   -d "text=おかえり"   -d "speaker=haruka"   -d "format=ogg"   -o voiceEnter.ogg
