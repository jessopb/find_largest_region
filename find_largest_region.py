from PIL import Image


def find_largest_region(image_file, paint_new):
    '''Returns the size of the largest contiguous color region in an image.
       If paint_new is true, it saves a new image with that region painted.
    '''

    largest_region = []
    largest_region.append([0])
    paint = paint_new
    global_px_visited = set()

    img = Image.open(image_file)
    xmax = img.size[0] - 1
    ymax = img.size[1] - 1

    def flood_region(coord):
        '''Wrapper for recursive flood-fill style alogorithm
        '''
        current_color = img.getpixel(coord)
        region_px_visited = set()

        def flood_recurse(coord):
            x, y = coord

            if img.getpixel(coord) != current_color:
                return
            # region_px_visited is a smaller set than global_px_visited
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
        # to output more comprehensive region data,
        # append region_px_visited set to list from here

        return region_px_visited

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            coord = (x, y)
            # global_px_visited says whether to bother with a pixel globally
            if coord not in global_px_visited:
                region_pixels = flood_region(coord)
                if len(region_pixels) > len(largest_region[0]):
                    largest_region[0] = region_pixels

    if paint is True:
        for point in largest_region[0]:
            img.putpixel((point), (255, 0, 0))
        img.save('newmap.bmp')
    print(largest_region[0])
    return len(largest_region[0])


def test():
    print('Largest Region has',
          find_largest_region('map1000.bmp', True),
          'pixels.')


if __name__ == '__main__':
    import time
    t = time.time()
    test()
    print('Time was', time.time() - t)
