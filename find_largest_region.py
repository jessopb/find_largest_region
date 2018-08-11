from PIL import Image

def find_largest_region(image_file):
    '''Returns the size of the largest contiguous color region in an image_file
    '''
    largest_region = 0
    global_px_visited = set()
    img = Image.open(image_file)
    #for debugging
    #debug_regions = []

    def flood_region(coord):
        '''Wrapper for recursive flood-fill style alogorithm
        '''
        current_color = img.getpixel(coord)
        region_px_visited = set()

        def flood_recurse(coord):
            x,y = coord
            xmax = img.size[0] - 1
            ymax = img.size[1] - 1

            if img.getpixel(coord) != current_color:
                return
            #region_px_visited is a smaller list than global_px_visited
            if coord in region_px_visited:
                return

            region_px_visited.add(coord)
            global_px_visited.add(coord)

            if y-1 >= 0:
                flood_recurse((x, y-1))
            if y+1 <= ymax:
                flood_recurse((x, y+1))
            if x-1 >= 0:
                flood_recurse((x-1, y))
            if x+1 <= xmax:
                flood_recurse((x+1, y))

        flood_recurse(coord)
        #for debugging:
        #debug_regions.append(region_px_visited)

        return len(region_px_visited)

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            coord = (x,y)
            #global_px_visited says whether to bother with a pixel globally
            if coord not in global_px_visited:
                size = flood_region(coord)
                if size > largest_region:
                    largest_region = size
    # for debugging:
    # for region in debug_regions:
    #     print(len(region),region)
    return largest_region

def test():
    print("Largest Region has", find_largest_region('map1.bmp'), 'pixels.')


if __name__ == '__main__':
    test()
