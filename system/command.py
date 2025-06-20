command_marker = "~*+"
passenger = "+*~"

passenger_data_end = '[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:chain_command_block",Properties:{facing:"up"}},TileEntityData:{Command:"~*+"},Time:1}]'
passenger_data = '[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:chain_command_block",Properties:{facing:"up"}},TileEntityData:{Command:"~*+"},Time:1,Passengers:+*~}]'
skip_data = '[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:sand"},Time:1,DropItem:0b,Passengers:+*~}]'



def create(data: list, auto_start: bool = True, starting_loc: str = "~ ~ ~2", looping: bool = False) -> str:
    until_skip = 0
    skip_index = 0
    #print(data)
    #print(auto_start)
    #print(starting_loc)
    #print(looping)
    if data:
        if auto_start:
            command_data = '/summon falling_block ' + starting_loc + ' {BlockState:{Name:"minecraft:barrier"},Time:1,Passengers:[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:command_block",Properties:{facing:"up"}},TileEntityData:{Command:"/fill ~1 ~1 ~ ~1 ~ ~ redstone_block"},Time:1,Passengers:+*~}]}'.replace("~1 ~ ~ ", f"~1 ~{len(data)} ~ ")
            command_data = command_data.replace(passenger, skip_data)
            until_skip = 2
            skip_sequens = [1, 2, 1, 2, 1, 2, 4]
        else:
            command_data = '/summon falling_block ' + starting_loc + ' {BlockState:{Name:"minecraft:command_block",Properties:{facing:"up"}},TileEntityData:{Command:"/fill ~1 ~1 ~ ~1 ~ ~ redstone_block"},Time:1,Passengers:+*~}'.replace("~1 ~ ~ ", f"~1 ~{len(data)} ~ ")
            until_skip = 1
            skip_sequens = [2, 1, 2, 1, 2, 4]
        for index in range(len(data)):
            command = data[index]
            if until_skip == 0:
                until_skip = skip_sequens[skip_index]
                skip_index += 1
                command_data = command_data.replace(passenger, skip_data)
            if index != len(data) - 1 or auto_start:
                if looping == True and index == 0:
                    command_data = command_data.replace(passenger, passenger_data.replace("chain_command_block", "repeating_command_block").replace(command_marker, command))
                else:
                    command_data = command_data.replace(passenger, passenger_data.replace(command_marker, command))
            else:
                if looping == True and index == 0:
                    command_data = command_data.replace(passenger, passenger_data_end.replace("chain_command_block", "repeating_command_block").replace(command_marker, command))
                else:
                    command_data = command_data.replace(passenger, passenger_data_end.replace(command_marker, command))
            until_skip -= 1
        if auto_start:
            if until_skip == 0:
                until_skip = skip_sequens[skip_index]
                skip_index += 1
                command_data = command_data.replace(passenger, skip_data)
            command_data = command_data.replace(passenger, '[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:redstone_block"},Time:1,Passengers:+*~}]')
            until_skip -= 1
            if until_skip == 0:
                until_skip = skip_sequens[skip_index]
                skip_index += 1
                command_data = command_data.replace(passenger, skip_data)
            command_data = command_data.replace(passenger, '[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:activator_rail"},Time:1,Passengers:+*~}]')
            until_skip -= 1
            command_data = command_data.replace(passenger, '[{id:"minecraft:command_block_minecart",Command:"/fill ~ ~ ~ ~ ~-15 ~ redstone_block replace barrier",Passengers:+*~}]')
            command_data = command_data.replace(passenger, '[{id:"minecraft:command_block_minecart",Command:"/kill @e[type=minecraft:command_block_minecart,sort=nearest,limit=2]"}]')

        return command_data
    
if __name__ == "__main__":
    command_data = create(["/say test"], auto_start=True)
    #print(command_data)