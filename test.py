# # import os


# filename = r".\audio\03d8ba1e-6929-441b-9f81-6e0030b7a8e3.wav"
# # os.system(f"ffmpeg -i {filename} -ar 16000 test.wav")

# from subprocess import Popen, PIPE

# with open(filename, "rb") as infile:
#     p=Popen(["ffmpeg", '-y', "-i", "-", "-ar", "16000", "test.wav"],
#         stdin=infile, stdout=PIPE)
# print(type(p), p)

s = "aA"
print(s[-1], s[-2])