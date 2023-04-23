# 1416. Restore The Array
# 🔴 Hard
#
# https://leetcode.com/problems/restore-the-array/
#
# Tags: String - Dynamic Programming

import timeit


# Iterate over possible combinations of left and right indexes checking
# if the resulting substring is a valid substring. We can improve the
# performance using dynamic programming, storing the number of
# valid combinations up to and including s[l] and adding that number to
# s[r+1] every time we find a valid substring s[l:r].
#
# Time complexity: O(log(k) * n) - We iterate over all n start positions
# in s, for each, we iterate over a maximum of log(k) values until the
# integer formed by the digits s[l:r] goes over k and we break.
# Space complexity: O(n) - The dp array has length n+1.
#
# Runtime 1335 ms Beats 89.4%
# Memory 18.1 MB Beats 82.19%
class DP:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [1] + [0] * (n)
        # Iterate over possible pairs of indexes.
        for l in range(n):
            # Ignore substrings that start with '0'.
            if s[l] == "0":
                continue
            num = 0
            for r in range(l, n):
                num = num * 10 + int(s[r])
                if num <= k:
                    # We can add s[r] to each all the ways we could
                    # build up to s[l].
                    dp[r + 1] = (dp[r + 1] + dp[l]) % (10**9 + 7)
                # If this value is bigger than k, no point moving left.
                else:
                    break

        return dp[-1]


# Optimize the previous solution using a dp array of size log(k) since
# we ever only go back log(k) positions to compute the current result.
#
# Time complexity: O(log(k) * n) - We iterate over all n start positions
# in s, for each, we iterate over a maximum of log(k) values until the
# integer formed by the digits s[l:r] goes over k and we break.
# Space complexity: O(log(k)) - The dp array has length log(k).
#
# Runtime 1323 ms Beats 89.4%
# Memory 14.8 MB Beats 100%
class DPO:
    def numberOfArrays(self, s: str, k: int) -> int:
        m, n = len(str(k)) + 1, len(s)
        dp = [0] * (m)
        dp[0] = 1
        # Iterate over possible pairs of indexes.
        for l in range(n):
            dpl = l % m
            # Ignore substrings that start with '0'.
            if s[l] == "0":
                dp[dpl] = 0
                continue
            num = 0
            for r in range(l, n):
                num = num * 10 + int(s[r])
                if num <= k:
                    dpr = (r + 1) % m
                    # We can add s[r] to each all the ways we could
                    # build up to s[l].
                    dp[dpr] = (dp[dpr] + dp[dpl]) % 1_000_000_007
                # If this value is bigger than k, no point moving left.
                else:
                    break
            # Clean up this position, it will be dp[dpr] next iteration.
            dp[dpl] = 0

        return dp[n % m]


def test():
    executors = [
        DP,
        DPO,
    ]
    tests = [
        ["1000", 10, 0],
        ["1000", 1000, 1],
        ["1317", 2000, 8],
        ["13171317", 20, 16],
        [
            "6300988793128824511853021957220525043738760339025464830436992222409273010074820428525903337547659862817693015346287473611171350478792555044497217960815838849076516688162655366051932735063562871843320664387124813714632299687044715551825863287405038147251907111874917204069665848665666233925003463722485316550243236974073761415182610484663155544191296815472240992501429260121549092974474880983985292015386126557135061114089246971903848384176471429735448746557617763264691548271882773124135021339325056315532626194600480449013211946481307429673757774567273679625443991337253991587037151246559169984786088553715839721570514221310653608195907452830650349826454340924850207371476286078176487871992644456344456054938161953567521994441594152142701012350146851013193951344995255248862792371361582545396392612783188553591390540872128690143819153437290639634184878177111408805953093976671779051904168121936105922515760573155558759894326902994495467245074458894730932131131523836486903591023402617206913797287365713835658073275699437889328261521735372020956227395160309147681335509670547207832056387516672567744776266946656559739917941766913605147740142291742429505791869111904587612233892332843448723267350306016072713793512161360227403732121133720206836823657005979572791532403266451149596123185878491580259333595043143349176463706299653386097433732948849773459334616786506952139391309955596374402795515813321445036745433074552286131362610984015914803279628112063671355720885250136792472586851153231355427420706767132495543049598372809536842772352299230588395212442452985900448544543435644923442152095808390424036818031275737503799163762099804643357752436584765464259224262215233746225246156798033484059797631309891360013523190963121636047256549980361843792707140181805254287382944411356136956646040802956881637605129820123217025443712791840386140625866035918605550092299648554759166046066486361314727774699190813869102462063183252153704872323356289327425023333252239346393652320603234372822161255793355711863675701205594417123714492085393626879045634791413635241919450398830636854521238576592363969863139277518034376603470930356869053961732306567975627336710148036535940343991036823006132497294417884562403903755929814204796636669753695422087024871",
            731671255,
            687537366,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numberOfArrays(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
