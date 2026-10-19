import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic" #윈도우는 Malgun Gothic
plt.rcParams["axes.unicode_minus"] = False

prices = [1000, 1500, 1800, 2400, 1900]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)

for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",xytext=(0, 8), ha="center")

ax.set_title("20235190_소선웅_점심가격변화")
fig.savefig("my_first_chart.png")
plt.close(fig)

print("그래프 저장 완료: my_first_chart.png")
