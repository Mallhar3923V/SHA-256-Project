from utils import *
def sha256(x):
    initial_hash = H_constants.copy()
    constants_K = K
    y = bytearray(preprocess(x))
    N = len(y)//64
    for i in range(N):
        chunk = y[i*64 : (i+1)*64]

        blocks = []
        a = 0
        b = 4
        while b <= 64:
            blocks.append(chunk[a:b])
            a+=4
            b+=4

        W = []
        for j in range(64):
            if j>=0 and j<=15 :
                W.append(int.from_bytes(blocks[j], byteorder = "big"))
            else:
                O = (little_sigma2(W[j-2]) + W[j-7] + little_sigma1(W[j-15]) + W[j-16]) & 0xFFFFFFFF
                W.append(O)

        A, B, C, D, E, F, G, H= initial_hash
       

        for n in range(64):
            #update each of A,B,C................
            T1 = (H + Big_sigma2(E) + ch(E,F,G) + constants_K[n] + W[n]) & 0xFFFFFFFF
            T2 = (Big_sigma1(A) + maj(A,B,C)) & 0xFFFFFFFF
            A, B, C, D, E, F, G, H = (T1 + T2) & 0xFFFFFFFF, A, B, C, (D + T1) & 0xFFFFFFFF, E, F, G


        current_state = [A, B, C, D, E, F, G, H]

        for idx in range(8):
            initial_hash[idx] = initial_hash[idx] + current_state[idx] & 0xFFFFFFFF

    Final = ""
    for val in initial_hash:
        Final += format(val, "08x")
   
    return Final

