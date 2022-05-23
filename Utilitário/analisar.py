eg = 0
tm = 0.0
ph = 0.0
tb = 0.0
op = 0.0
ct = 0.0
vz = 0.0
nv = 0.0
nh = 0.0
bd = 0.0

def analise(bd, nh, tb, vz, nv):
    if bd >= 20 and bd <= 30:
        if nh >= 20 and nh <= 30:
            if tb >= 0 and tb <= 5:
                if vz >= 20 and vz <= 30:
                    if nv == 1:
                        return 'boa'
                    else:
                        return 'mediana'
                elif (vz >= 10 and vz < 20) or (vz > 30 and vz <= 40):
                    return 'mediana'
                else:
                    return 'ruim'
            elif (tb > 5 and tb <= 10):
                return 'mediana'
            else:
                return 'ruim'
        elif (nh >= 10 and nh < 20) or (nh > 30 and nh <= 40):
            return 'mediana'
        else:
            return 'ruim'
    elif (bd >= 10 and bd < 20) or (bd > 30 and bd <= 40):
        return 'mediana'
    else:
        return 'ruim'
    
'''def analise(nh, tb, nv, tp, ph, op, bd):
    if nh >= 20 and nh <= 30:
        if tb >= 0 and tb <= 5:
                if nv == 1:
                    if tp >= 20 and tp <= 30:
                        if ph >= 7 and ph <= 10:
                            if op >= 20 and op <= 30:
                                if bd >= 20 and bd <= 30:
                                    return 'boa'
                                elif (bd >= 10 and bd < 20) or (bd < 30 and bd <= 40):
                                    return 'mediana'
                                else:
                                    return 'ruim'
                            elif (op >= 10 and op < 20) or (op > 30 and op <= 40):
                                return 'mediana'
                            else:
                                return 'ruim'
                        elif (ph >= 6 and ph < 7) or (ph > 10 and ph <= 11):
                            return 'mediana'
                        else:
                            return 'ruim'
                    elif (tp >= 10 and tp < 20) or (tp > 30 and tp <= 40):
                        return 'mediana'
                    else:
                        return 'ruim'
                else:
                    return 'mediana'
        elif (tb > 5 and tb <= 10):
            return 'mediana'
        else:
            return 'ruim'
    elif (nh >= 10 and nh < 20) or (nh > 30 and nh <= 40):
        return 'mediana'
    else:
        return 'ruim'

def analise (nh, tb, nv, ph, op, bd, ct):
    if nh >= 20 and nh <= 30:
        if tb >= 0 and tb <= 5:
            if nv == 1:
                if ph >= 7 and ph <= 10:
                    if op >= 20 and op <= 30:
                        if bd >= 20 and bd <= 30:
                            if ct >= 20 and ct <= 30:
                                return 'boa'
                            elif (ct >= 10 and ct < 20) or (ct > 30 and ct <= 40):
                                return 'mediana'
                            else:
                                return 'ruim'
                        elif (bd >= 10 and bd < 20) or (bd < 30 and bd <= 40):
                            return 'mediana'
                        else:
                            return 'ruim'
                    elif (op >= 10 and op < 20) or (op > 30 and op <= 40):
                        return 'mediana'
                    else:
                        return 'ruim'
                elif (ph >= 6 and ph < 7) or (ph > 10 and ph <= 11):
                    return 'mediana'
                else:
                    return 'ruim'
            else:
                return 'mediana'
        elif (tb > 5 and tb <= 10):
            return 'mediana'
        else:
            return 'ruim'
    elif (nh >= 10 and nh < 20) or (nh > 30 and nh <= 40):
        return 'mediana'
    else:
        return 'ruim'
'''