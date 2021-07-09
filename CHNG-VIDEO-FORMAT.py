import subprocess as subp

pth = "E:/MY-PROG/PRO-4-3-2019/TS~1/"
FN = "record"

with open("E:/MY-PROG/PRO-4-3-2019/TS~1/video.ts", 'wb') as f:
    for i in range(1, 8):
        with open(f"E:/MY-PROG/PRO-4-3-2019/TS~1/record.ts{i}", 'rb') as f1:
            data = f1.read()

        f.write(data)

subp.run(['ffmpeg', '-i', 'E:/MY-PROG/PRO-4-3-2019/TS~1/video.ts',
          'E:/MY-PROG/PRO-4-3-2019/TS~1/video.mp4'])
