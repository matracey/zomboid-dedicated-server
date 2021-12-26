# Zomboid Dedicated Server

## Disclaimer

**Note:** This image is not officially supported by Valve, nor by The Indie Stone.

If issues are encountered, please report them on
the [GitHub repository](https://github.com/Renegade-Master/zomboid-dedicated-server/issues/new/choose)

## Description

Dedicated Server for Zomboid using Docker, and optionally Docker-Compose.  
Built almost from scratch to be the smallest Zomboid Dedicated Server around!

## Links

Source:

- [GitHub](https://github.com/Renegade-Master/zomboid-dedicated-server)
- [DockerHub](https://hub.docker.com/r/renegademaster/zomboid-dedicated-server)

Resource links:

- [Dedicated Server Wiki](https://pzwiki.net/wiki/Dedicated_Server)
- [Dedicated Server Configuration](https://pzwiki.net/wiki/Server_Settings)
- [Steam DB Page](https://steamdb.info/app/380870/)

## Instructions

### Docker

The following are instructions for running the server using the Docker image.

1. Acquire the image locally:
    * Pull the image from DockerHub:

      ```shell
      docker pull renegademaster/zomboid-dedicated-server:<tagname>
      ```
    * Or alternatively, build the image:

      ```shell
      git clone https://github.com/Renegade-Master/zomboid-dedicated-server.git \
          && cd zomboid-dedicated-server

      docker build -t renegademaster/zomboid-dedicated-server:<tag> -f docker/zomboid-dedicated-server.Dockerfile .
      ```

2. Run the container interactively:  
   *Optional arguments table*:

   | Argument            | Description                                    | Values        | Default       |
   |---------------------|------------------------------------------------|---------------|---------------|
   | `BIND_IP`           | IP to bind the server to                       | 127.0.0.1     | 0.0.0.0       |
   | `GAME_VERSION`      | Game version to serve                          | [a-zA-Z0-9_]+ | `public`      |
   | `QUERY_PORT`        | Port for other players to connect to           | 1000 - 65535  | 16261         |
   | `GAME_PORT`         | Port for sending game data to clients          | 1000 - 65535  | 8766          |
   | `SERVER_NAME`       | Publicly visible Server Name                   | [a-zA-Z0-9]+  | ZomboidServer |
   | `SERVER_Password`   | Server password                                | [a-zA-Z0-9]+  |               |
   | `AUTOSAVE_INTERVAL` | Interval between autosaves in minutes          | [0-9]+        | 10m           |
   | `CAR_SPAWN_RATE`    | Frequency of car spawns                        | 1 - 5         | 10m           |
   | `MAX_PLAYERS`       | Maximum players allowed in the Server          | [0-9]+        | 16            |
   | `MAX_RAM`           | Maximum amount of RAM to be used               | ([0-9]+)m     | 4096m         |
   | `PAUSE_ON_EMPTY`    | Pause the Server when no Players are connected | (true\|false) | true          |
   | `PLAYER_SAFEHOUSE`  | Allow Players to claim Safehouses              | (true\|false) | true          |
   | `SAFEHOUSE_RESPAWN` | Allow Players to respawn in their Safehouse    | (true\|false) | true          |
   | `SLEEP_ALLOWED`     | Allow Players to sleep until morning           | (true\|false) | true          |
   | `STARTER_KIT`       | Allow Players to respawn with a Starter Kit    | (true\|false) | true          |
   | `WEAPON_MULTI_HIT`  | Allow large weapons to hit multiple Zomboids   | (true\|false) | true          |

   ***Note**: Arguments inside square brackets are optional. If the default ports are to be overridden, then the
   `published` ports below must also be changed*  

   ***Note 2**: It is currently not possible to automatically provide an admin password. This means that the game 
   must be run INTERACTIVELY the first time in order to set the admin password, but can be run headless every time 
   after that.* 

   ```shell
   mkdir ZomboidConfig ZomboidDedicatedServer

   docker run -it \
       --mount type=bind,source="$(pwd)/ZomboidDedicatedServer",target=/home/steam/ZomboidDedicatedServer \
       --mount type=bind,source="$(pwd)/ZomboidConfig",target=/home/steam/Zomboid \
       --publish 16261:16261/udp --publish 8766:8766/udp \
       --name zomboid-server \
       --user=$(id -u):$(id -g) \
       [--env=BIND_IP=<value>] \
       [--env=GAME_VERSION=<value>] \
       [--env=QUERY_PORT=<value>] \
       [--env=GAME_PORT=<value>] \
       [--env=SERVER_NAME=<value>] \
       [--env=SERVER_PASSWORD=<value>] \
       [--env=AUTOSAVE_INTERVAL=<value>] \
       [--env=CAR_SPAWN_RATE=<value>] \
       [--env=MAX_PLAYERS=<value>] \
       [--env=MAX_RAM=<value>] \
       [--env=PAUSE_ON_EMPTY=<value>] \
       [--env=PLAYER_SAFEHOUSE=<value>] \
       [--env=SAFEHOUSE_RESPAWN=<value>] \
       [--env=SLEEP_ALLOWED=<value>] \
       [--env=STARTER_KIT=<value>] \
       [--env=WEAPON_MULTI_HIT=<value>] \
       renegademaster/zomboid-dedicated-server[:<tagname>]
   ```

3. Wait to be prompted to enter the admin password. Set this to something that you will remember.

4. Once you see `znet: Zomboid Server is VAC Secure` in the console press `CTRL + C` to stop the server.

5. Run the container headless:

   ```shell
   docker run --detach \
       --mount type=bind,source="$(pwd)/ZomboidDedicatedServer",target=/home/steam/ZomboidDedicatedServer \
       --mount type=bind,source="$(pwd)/ZomboidConfig",target=/home/steam/Zomboid \
       --publish 16261:16261/udp --publish 8766:8766/udp \
       --name zomboid-server \
       --user=$(id -u):$(id -g) \
       [--env=BIND_IP=<value>] \
       [--env=GAME_VERSION=<value>] \
       [--env=QUERY_PORT=<value>] \
       [--env=GAME_PORT=<value>] \
       [--env=SERVER_NAME=<value>] \
       [--env=SERVER_PASSWORD=<value>] \
       [--env=AUTOSAVE_INTERVAL=<value>] \
       [--env=CAR_SPAWN_RATE=<value>] \
       [--env=MAX_PLAYERS=<value>] \
       [--env=MAX_RAM=<value>] \
       [--env=PAUSE_ON_EMPTY=<value>] \
       [--env=PLAYER_SAFEHOUSE=<value>] \
       [--env=SAFEHOUSE_RESPAWN=<value>] \
       [--env=SLEEP_ALLOWED=<value>] \
       [--env=STARTER_KIT=<value>] \
       [--env=WEAPON_MULTI_HIT=<value>] \
       renegademaster/zomboid-dedicated-server[:<tagname>]
   ```

### Docker-Compose

The following are instructions for running the server using Docker-Compose.

1. Download the repository:

   ```shell
   git clone https://github.com/Renegade-Master/zomboid-dedicated-server.git \
       && cd zomboid-dedicated-server
   ```

2. Make any configuration changes you want to in the `docker-compose.yaml` file. In
   the `services.zomboid-server.environment` section, you can change values for:

   | Argument            | Description                                    | Values        | Default       |
   |---------------------|------------------------------------------------|---------------|---------------|
   | `BIND_IP`           | IP to bind the server to                       | 127.0.0.1     | 0.0.0.0       |
   | `GAME_VERSION`      | Game version to serve                          | [a-zA-Z0-9_]+ | `public`      |
   | `QUERY_PORT`        | Port for other players to connect to           | 1000 - 65535  | 16261         |
   | `GAME_PORT`         | Port for sending game data to clients          | 1000 - 65535  | 8766          |
   | `SERVER_NAME`       | Publicly visible Server Name                   | [a-zA-Z0-9]+  | ZomboidServer |
   | `SERVER_Password`   | Server password                                | [a-zA-Z0-9]+  |               |
   | `AUTOSAVE_INTERVAL` | Interval between autosaves in minutes          | [0-9]+        | 10m           |
   | `CAR_SPAWN_RATE`    | Frequency of car spawns                        | 1 - 5         | 10m           |
   | `MAX_PLAYERS`       | Maximum players allowed in the Server          | [0-9]+        | 16            |
   | `MAX_RAM`           | Maximum amount of RAM to be used               | ([0-9]+)m     | 4096m         |
   | `PAUSE_ON_EMPTY`    | Pause the Server when no Players are connected | (true\|false) | true          |
   | `PLAYER_SAFEHOUSE`  | Allow Players to claim Safehouses              | (true\|false) | true          |
   | `SAFEHOUSE_RESPAWN` | Allow Players to respawn in their Safehouse    | (true\|false) | true          |
   | `SLEEP_ALLOWED`     | Allow Players to sleep until morning           | (true\|false) | true          |
   | `STARTER_KIT`       | Allow Players to respawn with a Starter Kit    | (true\|false) | true          |
   | `WEAPON_MULTI_HIT`  | Allow large weapons to hit multiple Zomboids   | (true\|false) | true          |

   ***Note**: If the default ports are to be overridden, then the `published` ports must also be changed*

3. In the `docker-compose.yaml` file, you must change the `service.zomboid-server.user` values to match your local user.
   To find your local user and group ids, run the following command:

   ```shell
   printf "UID: %s\nGID: %s\n" $(id -u) $(id -g)
   ```

4. Run the following commands:

   ```shell
   mkdir ZomboidConfig ZomboidDedicatedServer

   docker-compose run zomboid-server /home/steam/ZomboidDedicatedServer/start-server.sh
   ```

5. Wait to be prompted to enter the admin password. Set this to something that you will remember.

6. Once you see `znet: Zomboid Server is VAC Secure` in the console press `CTRL + C` to stop the server.

7. Run the following command to start the server headless:

   ```shell
   docker-compose up --detach
   ```
