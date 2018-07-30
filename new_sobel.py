def new_sobel(input) :
    # input mode is gray or luminance
    h, w = input.shape

    sb_filter = np.zeros((4, 3, 3))
    out = np.zeros((4, h, w))
    sb_filter[0] = np.array(([1, 2, 1], [0, 0, 0], [-1, -2, -1]))
    sb_filter[1] = np.array(([0, 1, 2], [-1, 0, 1], [-2, -1, 0]))
    sb_filter[2] = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]))
    sb_filter[3] = np.array(([-2, -1, 0], [-1, 0, 1], [0, 1, 2]))
    bg = np.pad(input, 1, 'edge')

    for i in range(4):
        for m in range(h):
            for n in range(w):
                out[i, m, n] = np.sum(bg[m:m+3, n:n+3] * sb_filter[i])

    X = np.hypot(np.hypot(out[0], out[1]), np.hypot(out[2], out[3]))

    return X
