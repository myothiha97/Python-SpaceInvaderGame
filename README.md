# Python-SpaceInvaderGame

![Game Logo]
(logo_img.png)

## Require Python3.8 or above

### For linux

**First Create VirtualEnv with require python version.**

```
virtualenv my_vir -p python_path/python3
```

**Then activate virtualenv by following command**

```
source my_vir/bin/activate
```

**After that, install require dependencies by following command**

```
pip install -r requirements.txt
```
### Game Rules
* Player has to hit enemy ship to get the score
* If the enemy ship reaches  the bottom , the game is over
* Player will won the game if the score is reached up to 10.
* The enemy ship respawn whenever it get hits by player

> The enemy respawn height will be maximum of 50-150.
> You can shoot only one bullet per time and wait for the bullet to hit the boundary.

### Key Bindings
* Left and Right arrow keys for left and right movement
* Space key for shooting bullet.

