# /bin/sh

# start web
tmux new-session -d  'cd ~/MyRobot2017Summer/web && npm run liveserver'

sleep 60

# start touchphat
tmux new-session -d 'python3 ~/MyRobot2017Summer/touchphat/buttons.py'

