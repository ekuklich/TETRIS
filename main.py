import pygame as pg
import time
import numpy as np
import random


def rot_part(sp, i, j, s):
    h = np.rot90(part(sp, i, j, k))
    for i1 in range(s):
        for j1 in range(s):
            sp[i1 + i][j1 + j] = h[i1][j1]
    return sp


def part(sp, i, j, s):
    ans = [[sp[i + i1][j + j1] for j1 in range(s)] for i1 in range(s)]
    return ans


def cnt(sp):
    ans = 0
    for i in sp:
        for j in i:
            if j == 1:
                ans += 1
    if ans == 4:
        return True
    return False


def tetr(sp, a=4):
    Index = 1
    a -= 1
    if sp == -1:
        return -1
    for _ in range(100):
        try:
            n, m = 0, len(sp) // 2
            for _ in range(1000):
                if sp[n][m] == 0:
                    break
                n, m = 0, len(sp) // 2

            v = [(n, m)]
            sp[n][m] = Index
            for i in range(a):
                v1 = []
                for j in v:
                    if (j[1] + 1) < len(sp):
                        if sp[j[0]][j[1] + 1] == 0:
                            v1.append((j[0], j[1] + 1))

                    if (j[1] - 1) >= 0:
                        if sp[j[0]][j[1] - 1] == 0:
                            v1.append((j[0], j[1] - 1))

                    if len(sp) > (j[0] + 1):
                        if sp[j[0] + 1][j[1]] == 0:
                            v1.append((j[0] + 1, j[1]))

                    if (j[0] - 1) >= 0:
                        if sp[j[0] - 1][j[1]] == 0:
                            v1.append((j[0] - 1, j[1]))

                # print(v1, "DO", *v)
                v1 = set(v1)
                v = set(v)
                v1 = v1 - v
                v1 = list(v1)
                v = list(v)
                k, l = v1[random.randint(0, len(v1) - 1)]
                # print(k, l)
                # print(v1)
                v.append((k, l))
                sp[k][l] = Index
                '''
                for i in v1:
                    v.append(i)
                    '''
            return sp
        except:
            pass
    return -1


def down(sp):
    for i in range(len(sp)):
        for j in range(len(sp[i])):
            if sp[i][j] == 1:
                if i + 1 < len(sp):
                    if sp[i + 1][j] == -1:
                        return False
                else:
                    return False
    return True


w, h = 600, 600
siz = 30
xxx = 3
win = pg.display.set_mode((w, h - (h // siz) * xxx))
sp = [[0 for _ in range(siz)] for _ in range(siz)]
rec = [[pg.Rect(i * (w // siz), j * (h // siz), w // siz, h // siz) for i in range(siz)] for j in range(siz)]
sp = tetr(sp)
pg.init()
tim = time.time()
while True:
    if time.time() - tim >= 0.2:
        tim = tim = time.time()
        if down(sp):
            for i in range(len(sp) - 1, -1, -1):
                for j in range(len(sp[i])):
                    if i + 1 < len(sp):
                        if sp[i][j] == 1:
                            sp[i][j], sp[i + 1][j] = sp[i + 1][j], sp[i][j]
        else:
            for i in range(len(sp)):
                for j in range(len(sp[i])):
                    if sp[i][j] == 1:
                        sp[i][j] = -1
            # sp[0][random.randint(0, siz - 1)] = 1
            sp = tetr(sp)
    for K in pg.event.get():
        if K.type == pg.QUIT:
            exit()
        if K.type == pg.KEYDOWN:
            if K.key == pg.K_RIGHT:
                do = True
                for i in range(len(sp)):
                    for j in range(len(sp[i])):
                        if sp[i][j] == 1:
                            if j + 1 >= len(sp[i]):
                                do = False
                                break
                            else:
                                if sp[i][j + 1] == -1:
                                    do = False
                                    break
                if do:
                    for i in range(len(sp)):
                        for j in range(len(sp[i]) - 1, -1, -1):
                            if sp[i][j] == 1 and j + 1 < len(sp[i]):
                                if sp[i][j + 1] != -1:
                                    sp[i][j], sp[i][j + 1] = sp[i][j + 1], sp[i][j]
            if K.key == pg.K_LEFT:
                do = True
                for i in range(len(sp)):
                    for j in range(len(sp[i])):
                        if sp[i][j] == 1:
                            if j - 1 < 0:
                                print(1)
                                do = False
                                break
                            else:
                                if sp[i][j - 1] == -1:
                                    do = False
                                    break
                if do:
                    for i in range(len(sp)):
                        for j in range(len(sp[i])):

                            if sp[i][j] == 1 and j - 1 >= 0:
                                if sp[i][j - 1] != -1:
                                    sp[i][j], sp[i][j - 1] = sp[i][j - 1], sp[i][j]
            if K.key == pg.K_DOWN:
                for _ in range(siz):
                    tim = tim = time.time()
                    if down(sp):
                        for i in range(len(sp) - 1, -1, -1):
                            for j in range(len(sp[i])):
                                if i + 1 < len(sp):
                                    if sp[i][j] == 1:
                                        sp[i][j], sp[i + 1][j] = sp[i + 1][j], sp[i][j]
                    else:
                        for i in range(len(sp)):
                            for j in range(len(sp[i])):
                                if sp[i][j] == 1:
                                    sp[i][j] = -1
                        sp = tetr(sp)
                        break

            if K.key == pg.K_UP:

                sp1 = [[sp[j][i] for i in range(len(sp[j]))] for j in range(len(sp))]
                do = True
                ext = False
                for k in range(2, 5):
                    if ext:
                        break
                    for i in range(len(sp) - k):
                        if ext:
                            break
                        for j in range(len(sp[i]) - k):
                            if ext:
                                break
                            if cnt(part(sp, i, j, k)):
                                # print(*part(sp,i,j,k), sep="\n")
                                sp1 = rot_part(sp1, i, j, k)
                                #print(sp1==sp)
                                for n in range(len(sp)):
                                    for m in range(len(sp[n])):
                                        #print(sp[n][m],sp1[n][m])
                                        if sp[n][m] == -1 and sp1[n][m] != sp[n][m]:
                                            print(1)
                                            do = False
                                            break
                                ext = True
                                break
                if do:
                    print("DA")
                    sp = sp1

    win.fill((0, 0, 0))
    for i in range(siz):
        for j in range(siz):
            if sp[i][j] == 0:
                pg.draw.rect(win, (100, 100, 100), rec[i][j].move(0, -(h // siz) * xxx))
            else:
                pg.draw.rect(win, (255, 0, 0), rec[i][j].move(0, -(h // siz) * xxx))
    pg.display.flip()
