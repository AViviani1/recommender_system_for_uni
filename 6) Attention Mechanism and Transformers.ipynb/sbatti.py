import numpy as np
import re 
fuck = '''
Epoch 001 time to train: 00: 00: 19
HR: 0.398 NDCG: 0.210
Epoch 002 time to train: 00: 00: 19
HR: 0.404 NDCG: 0.223
Epoch 003 time to train: 00: 00: 18
HR: 0.413 NDCG: 0.220
Epoch 004 time to train: 00: 00: 20
HR: 0.408 NDCG: 0.218
Epoch 005 time to train: 00: 00: 18
HR: 0.415 NDCG: 0.227
Epoch 006 time to train: 00: 00: 18
HR: 0.439 NDCG: 0.232
Epoch 007 time to train: 00: 00: 19
HR: 0.446 NDCG: 0.239
Epoch 008 time to train: 00: 00: 18
HR: 0.472 NDCG: 0.255
Epoch 009 time to train: 00: 00: 19
HR: 0.469 NDCG: 0.258
Epoch 010 time to train: 00: 00: 18
HR: 0.483 NDCG: 0.266
Epoch 011 time to train: 00: 00: 19
HR: 0.498 NDCG: 0.272
Epoch 012 time to train: 00: 00: 19
HR: 0.498 NDCG: 0.276
Epoch 013 time to train: 00: 00: 18
HR: 0.514 NDCG: 0.285
Epoch 014 time to train: 00: 00: 21
HR: 0.529 NDCG: 0.290
Epoch 015 time to train: 00: 00: 18
HR: 0.527 NDCG: 0.297
Epoch 016 time to train: 00: 00: 20
HR: 0.525 NDCG: 0.296
Epoch 017 time to train: 00: 00: 19
HR: 0.530 NDCG: 0.302
Epoch 018 time to train: 00: 00: 20
HR: 0.542 NDCG: 0.306
Epoch 019 time to train: 00: 00: 18
HR: 0.546 NDCG: 0.306
Epoch 020 time to train: 00: 00: 18
HR: 0.542 NDCG: 0.304
Epoch 021 time to train: 00: 00: 19
HR: 0.547 NDCG: 0.311
Epoch 022 time to train: 00: 00: 18
HR: 0.556 NDCG: 0.315
Epoch 023 time to train: 00: 00: 19
HR: 0.555 NDCG: 0.317
Epoch 024 time to train: 00: 00: 18
HR: 0.573 NDCG: 0.321
Epoch 025 time to train: 00: 00: 19
HR: 0.561 NDCG: 0.317
Epoch 026 time to train: 00: 00: 20
HR: 0.575 NDCG: 0.323
Epoch 027 time to train: 00: 00: 18
HR: 0.577 NDCG: 0.322
Epoch 028 time to train: 00: 00: 20
HR: 0.569 NDCG: 0.317
Epoch 029 time to train: 00: 00: 18
HR: 0.562 NDCG: 0.319
Epoch 030 time to train: 00: 00: 19
HR: 0.567 NDCG: 0.321
'''
x = re.findall("\d.\d+[\n]", fuck)
x2 = []
for i in x:
    i = float(i.replace('\n',''))
    x2.append(i)
#print(x2)

x = re.findall("[R,:][R,:].\d.\d+", fuck)
x2 = []
for i in x:
    print(i)
    i = float(i.replace('R: ',''))
    x2.append(i)
print(x2)
