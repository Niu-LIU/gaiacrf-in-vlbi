# UT1
fig, (ax0, ax1, ax2) = plt.subplots(figsize=(12, 12), sharex=True, nrows=3)

# Error bar plot
ax0.errorbar(pmrEpoch.jyear,
             ngaeoboft["dut"],
             yerr=ngaeoboft["dut_err"],
             fmt="b.",
             ms=1,
             elinewidth=0.05,
             ecolor="k",
             errorevery=5)

# Offset
ax1.plot(pmrEpoch.jyear, ngaeoboft["dut"], "b.", ms=1)
epomed = bn.move_median(pmrEpoch.jyear, window=50)
dutmed = bn.move_median(ngaeoboft["dut"], window=50)
ax1.plot(epomed, dutmed, "r")


# Formal error
ax2.plot(pmrEpoch.jyear, ngaeoboft["dut_err"], "b.", ms=1)
duterrmed = bn.move_median(ngaeoboft["dut_err"], window=50)
ax2.plot(epomed, duterrmed, "r")


# Add a horizontal line
x = np.arange(1979, 2021, 0.5)
y0 = np.zeros_like(x)
ax0.plot(x, y0, "r", lw=1)

# Add a fitted line
# x0 = np.arange(1979, 2021, 1)
# y0 = x0 * 0.2 - 403
# ax.plot(x0, y0, "r", lw=2)

ax2.set_yscale("log")

# Limits
ax0.axis([1979, 2020, -5, 5])
ax1.set_ylim([-1, 1])
# ax2.set_ylim([30, 40000])

# Titles and Labels
ax0.set_title("$UT1$ (icrf2ga $-$ icrf3ga)")
ax0.set_ylabel("$\mu$s")
ax1.set_ylabel("Offset [$\mu$s]")
ax2.set_ylabel("Errors [$\mu$s]")
ax2.set_xlabel("Year")

# Ticks
ax0.xaxis.set_ticks_position("both")
ax0.yaxis.set_ticks_position("both")

ax1.xaxis.set_ticks_position("both")
ax1.yaxis.set_ticks_position("both")

ax2.xaxis.set_ticks_position("both")
ax2.yaxis.set_ticks_position("both")

# Add minor ticks
ax0.xaxis.set_minor_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(MultipleLocator(0.5))

# Add grid
# ax0.grid()
ax1.grid()
ax2.grid()
