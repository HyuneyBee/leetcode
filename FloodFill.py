class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        origin_color = image[sr][sc]
        check_image = [[False for _ in range(len(image[0]))] for _ in range(len(image))]

        dsr = [-1, 0, 1, 0]
        dsc = [0, 1, 0, -1]
        def dfs(sr, sc):
            check_image[sr][sc] = True
            image[sr][sc] = color

            for i in range(4):
                nsr = sr + dsr[i]
                nsc = sc + dsc[i]

                if 0 <= nsr < len(image) and 0 <= nsc < len(image[0]) and not check_image[nsr][nsc] and image[nsr][nsc] == origin_color:
                    dfs(nsr, nsc)

        dfs(sr, sc)

        return image


def main() -> None:
    result = Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2)
    print(result)


if __name__ == "__main__":
    main()