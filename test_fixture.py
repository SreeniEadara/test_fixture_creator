from kiutils import board
import os

# Get input .kicad_pcb
file_path = input("Specify full path of parent .kicad_pcb file\n").strip()

if not(os.path.isfile(file_path)):
    print("Invalid path")
    exit()

original_pcb = board.Board().from_file(file_path)
new_pcb = board.Board()

# Copy edge cuts layer
for item in original_pcb.graphicItems:
    if item.layer == 'Edge.Cuts':
        new_pcb.graphicItems.append(item)

nets_for_test = []

# Copy test points over. These can be replaced by a desired pogo pin connector
for footprint in original_pcb.footprints:
    if footprint.libraryNickname == 'TestPoint':
        new_pcb.footprints.append(footprint)
        for pad in footprint.pads:
            nets_for_test.append(pad.net)
            
# Copy tested nets to new file
new_pcb.nets = nets_for_test

# Copy settings from old file to new file
new_pcb.version = original_pcb.version
new_pcb.dimensions = original_pcb.dimensions
new_pcb.general = original_pcb.general
new_pcb.generator = original_pcb.generator
new_pcb.layers = original_pcb.layers

# Save new file
save_path = input("Specify full path to save test fixture pcb.\nIf none specified, will save to same directory\n")
save_path = save_path.strip()

if save_path == '' or not(os.path.isfile(save_path)):
    print("None specified or invalid path. Saving to same directory")
    save_path = file_path.split(".")
    file_extension = save_path.pop()
    save_path.append("_test_fixture.")
    save_path.append(file_extension)
    save_path = "".join(save_path)

new_pcb.to_file(save_path)
print("Saved at " + save_path)
