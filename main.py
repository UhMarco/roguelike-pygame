import pygame
import random

from bersenham import get_line
from blueprints import blueprints, exit_blueprint

TILE_SIZE = 28
WORLD_SIZE = TILE_SIZE * 8 * 5
SIZE = 900

pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE))
clock = pygame.time.Clock()
fps = 30

font = pygame.font.Font("./assets/KLEINTEN.ttf", 32)
font_lg = pygame.font.Font("./assets/KLEINTEN.ttf", 64)
FONT_COLOUR = (153, 167, 153)

# Images
IMAGE_SIZE = (TILE_SIZE, TILE_SIZE)

player_img = pygame.transform.scale(
    pygame.image.load("./assets/knight.png"), IMAGE_SIZE
)
door_img = pygame.transform.scale(pygame.image.load("./assets/door.png"), IMAGE_SIZE)
exit_img = pygame.transform.scale(pygame.image.load("./assets/exit.png"), IMAGE_SIZE)
key_img = pygame.transform.scale(pygame.image.load("./assets/key.png"), IMAGE_SIZE)
potion_img = pygame.transform.scale(pygame.image.load("./assets/potion.png"), IMAGE_SIZE)

enemy_img = pygame.transform.scale(pygame.image.load("./assets/enemy.png"), IMAGE_SIZE)
enemy_img_angry = pygame.transform.scale(pygame.image.load("./assets/enemy_angry.png"), IMAGE_SIZE)
walls = []
for i in range(4):
    walls.append(
        pygame.transform.scale(
            pygame.image.load(f"./assets/wall{i + 1}.png"), IMAGE_SIZE
        )
    )

UI_SIZE = (TILE_SIZE * 2, TILE_SIZE * 2)
UI_OFFSET = 10

key_ui = pygame.transform.scale(pygame.image.load("./assets/key.png"), UI_SIZE)
potion_ui = pygame.transform.scale(pygame.image.load("./assets/potion.png"), UI_SIZE)

pygame.display.set_caption("Dungeon")
pygame.display.set_icon(player_img)

# Main
LEVELS = 5
current_level = 1

while current_level <= LEVELS:

    # Generate rooms
    def get_adjacent(index):
        result = [index + 1, index - 1, index + 5, index - 5]

        for item in result:
            if item > 24 or item < 0:
                result.remove(item)
        
        if index % 5 == 0 and index - 1 in result:
            result.remove(index - 1)
        elif (index + 1) % 5 == 0 and index + 1 in result:
            result.remove(index + 1)

        return result

    def generate_rooms(desired_rooms):
        grid = [0] * 25

        # start from center
        grid[12] = 1
        desired_rooms -= 1
        adjacent = get_adjacent(12)

        while desired_rooms > 0:
            # check adjacent array twice
            # for some reason if either one is there alone, arrays change at times they shouldn't
            for index in adjacent:
                if grid[index] == 1:
                    adjacent.remove(index)
            
            # get random room from adjacent cells
            next_room = random.choice(adjacent)

            grid[next_room] = 1 if desired_rooms > 1 else 2

            # add new adjacents to list
            adjacent.extend(get_adjacent(next_room))
            adjacent = list(set(adjacent))

            for index in adjacent:
                if grid[index] == 1:
                    adjacent.remove(index)

            desired_rooms -= 1

        for i in range(len(grid)):
            if grid[i] in [1, 2]: # 1: normal room / 2: exit room
                blueprint = random.choice(blueprints).copy() if grid[i] == 1 else exit_blueprint.copy()

                # left
                if i % 5 != 0 and grid[i - 1]:
                    blueprint[24] = 0
                    blueprint[32] = 0

                # right
                if (i + 1) % 5 != 0 and grid[i + 1]:
                    blueprint[31] = 0
                    blueprint[39] = 0

                # up
                if i > 4 and grid[i - 5]:
                    blueprint[3] = 0
                    blueprint[4] = 0

                # down
                if i < 20 and grid[i + 5]:
                    blueprint[59] = 0
                    blueprint[60] = 0

                # random wall variation
                for j in range(len(blueprint)):
                    if blueprint[j] == 1 and random.randint(0, 7) == 0:
                        blueprint[j] = random.choice([2, 3, 4])
                
                grid[i] = blueprint

        

        return grid

    ROOM_NUM = 5 + current_level
    world = generate_rooms(ROOM_NUM)

    room_indexes = []
    for i in range(len(world)):
        if world[i]:
            room_indexes.append(i)

    player_x = SIZE / 2 - TILE_SIZE / 2
    player_y = SIZE / 2 - TILE_SIZE / 2
    player_pos = 0
    player_keys = 0
    player_potions = 0
    player_steps = 2
    player_flipped = False

    offset_x = (SIZE - WORLD_SIZE) / 2 + TILE_SIZE * 4 - TILE_SIZE / 2
    offset_y = (SIZE - WORLD_SIZE) / 2 + TILE_SIZE * 4 - TILE_SIZE / 2

    # Find the spawn point in the centre room
    centre_room = world[12]
    for i in range(len(centre_room)):
        if centre_room[i] == 10:
            offset_x -= i % 8 * TILE_SIZE
            offset_y -= int(i / 8) * TILE_SIZE
            player_pos = (8 * 5 * 16 + 16) + i % 8 + int(i / 8) * (8 * 5)
            break

    room_indexes.remove(12)

    # Key spawns
    key_indexes = room_indexes.copy()
    for i in range(3):
        index = random.choice(key_indexes)
        room = world[index]
        key_indexes.remove(index)
        for j in range(len(room)):
            if room[j] == 12:
                room[j] = 16

    # Bomb spawns
    bomb_indexes = room_indexes.copy()
    for i in range(3):
        index = random.choice(bomb_indexes)
        room = world[index]
        bomb_indexes.remove(index)
        for j in range(len(room)):
            if room[j] == 13:
                room[j] = 17

    # Enemy spawns
    enemy_indexes = room_indexes.copy()
    for i in range(2 + current_level):
        index = random.choice(enemy_indexes)
        room = world[index]
        enemy_indexes.remove(index)
        for j in range(len(room)):
            if room[j] == 11:
                room[j] = 15


    # Convert world into 1D array
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    new_world = []

    for y in range(5):
        for room_y in range(8):
            for x in range(5):
                room = world[(y * 5) + x]
                room_chunks = [[0] * 8] * 8
                if room:
                    room_chunks = list(chunks(room, 8))
                new_world.extend(room_chunks[room_y])

    world = new_world

    wall_tiles = []
    c = 0
    for i in range(len(walls)):
        c += 1
        wall_tiles.append(c)
    
    def get_distance(c1, c2):
        return (((c2[0] - c1[0] ) ** 2) + ((c2[1] - c1[1]) ** 2) ) ** 0.5

    # Play
    game_over = False
    running = True
    while running:
        clock.tick(fps)

        player_start = player_pos

        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                current_level = LEVELS
                running = False

            if event.type == pygame.KEYDOWN and player_steps and not game_over:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    player_flipped = True
                    if world[player_pos - 1] not in wall_tiles:
                        # Walks into door
                        if world[player_pos - 1] == 30:
                            if player_keys > 0:
                                player_keys -= 1
                                world[player_pos - 1] = 0
                                offset_x += TILE_SIZE
                                player_pos -= 1

                        else:
                            offset_x += TILE_SIZE
                            player_pos -= 1

                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    player_flipped = False
                    if world[player_pos + 1] not in wall_tiles:
                        offset_x -= TILE_SIZE
                        player_pos += 1

                elif event.key in [pygame.K_UP, pygame.K_w]:
                    if world[player_pos - (8 * 5)] not in wall_tiles:
                        # Walks into exit
                        if world[player_pos - (8 * 5)] == 31:
                            # Level complete
                            running = False

                        offset_y += TILE_SIZE
                        player_pos -= 8 * 5

                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    if world[player_pos + (8 * 5)] not in wall_tiles:
                        offset_y -= TILE_SIZE
                        player_pos += 8 * 5 

        if int(world[player_pos]) == 15:
            game_over = True

        elif world[player_pos] == 16:
            world[player_pos] = 0
            player_keys += 1

        if player_start != player_pos:
            player_steps -= 1

        if player_steps == 0:
            # Enemy turn
            new_world = world.copy()
            for i in range(len(world)):
                if int(world[i]) == 15:
                    # Enemy
                    e_pos = (i % (8 * 5), int(i / (8 * 5)))
                    p_pos = (player_pos % (8 * 5), int(player_pos / (8 * 5)))
                    path = get_line(e_pos, p_pos)
                    sight = True
                    for coord in path:
                        if world[(coord[1] * 8 * 5) + coord[0]] in wall_tiles:
                            sight = False
                            break

                    if sight:
                        moves = []
                        moves.append((e_pos[0] + 1, e_pos[1]))
                        moves.append((e_pos[0], e_pos[1] + 1))
                        moves.append((e_pos[0] - 1, e_pos[1]))
                        moves.append((e_pos[0], e_pos[1] - 1))

                        best_move = ()
                        best_distance = get_distance(e_pos, p_pos)

                        for move in moves:
                            if get_distance(move, p_pos) < best_distance and world[move[1] * (8 * 5) + move[0]] in [0, 10, 11, 12, 13, 14]:
                                best_distance = get_distance(move, p_pos)
                                best_move = move

                        if best_move != ():
                            new_world[i] = 0
                            if new_world[best_move[1] * (8 * 5) + best_move[0]] == p_pos:
                                game_over = True
                            new_world[best_move[1] * (8 * 5) + best_move[0]] = 15.1

                    else:
                        new_world[i] = 15

            world = new_world
            player_steps = 2

        # Background
        screen.fill((237, 228, 210))

      
        # Player
        screen.blit(pygame.transform.flip(player_img, player_flipped, False), (player_x, player_y))

        # Render world
        for i in range(len(world)):
            tile = world[i]
            tile_x = i % (8 * 5) * TILE_SIZE
            tile_y = int(i / (8 * 5)) * TILE_SIZE
            tile_pos = (tile_x + offset_x, tile_y + offset_y)

            if 1 <= tile <= len(walls):
                screen.blit(walls[tile - 1], tile_pos)
            elif tile == 15:
                screen.blit(enemy_img, tile_pos)
            elif tile == 15.1:
                screen.blit(enemy_img_angry, tile_pos)
            elif tile == 16:
                screen.blit(key_img, tile_pos)
            elif tile == 17:
                screen.blit(potion_img, tile_pos)
            elif tile == 30:
                screen.blit(door_img, tile_pos)
            elif tile == 31:
                screen.blit(exit_img, tile_pos)

        # Render UI
        text = font.render("Steps:", False, FONT_COLOUR)
        screen.blit(text, (UI_OFFSET, UI_OFFSET))
        text = font.render(str(player_steps), False, FONT_COLOUR)
        screen.blit(text, (UI_OFFSET * 10.3, UI_OFFSET))
        text = font.render("Level:", False, FONT_COLOUR)
        screen.blit(text, (UI_OFFSET, UI_OFFSET * 5.5))
        text = font.render(str(current_level), False, FONT_COLOUR)
        screen.blit(text, (UI_OFFSET * 10.3, UI_OFFSET * 5.5))
        for i in range(player_keys):
            screen.blit(key_ui, (UI_SIZE[0] * i, UI_OFFSET * 9))

        if game_over:
            text = font_lg.render("Game Over!", False, FONT_COLOUR)
            screen.blit(text, (SIZE / 2 - text.get_rect().width / 2, SIZE / 2 - text.get_rect().height / 2))

        pygame.display.update()

    # Level complete
    current_level += 1


pygame.quit()
quit()
