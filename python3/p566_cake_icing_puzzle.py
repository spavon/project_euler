def flip_pieces(a, b, c):
    cake = [1 for i in range(1,361)]
    save = 0
    count = 0
    tf = True
    while tf:
        for x in a,b,c:
            print(save, x+save)
            for j in range(save, x + save):
                #print("Index: ", j)
                cake[j] *= -1
            cake[save:x + save:-1]
            print("Save before: ", save)
            # Need to deal with cases when slicing overlaps with the start of the array
            save = (save + x) % 360
            print("Save after: ", save)
            #save = turn_over(save, x)
        count += 1
        if not (-1 in cake):
            print(count)
            tf = False
        #print(cake)
        if(count == 60):
            tf = False



flip_pieces(9,10,11)
#flip_pieces(10,14,16)

if __name__ == '__main__':
    main()
