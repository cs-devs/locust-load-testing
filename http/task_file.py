from locust import HttpUser, between, task
class WebsiteUser(HttpUser):
    wait_time = between(0, 5)

    @task(1)
    def ManageLookups(self):
        self.client.get('api/ManageLookups', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def Lookup(self):
        self.client.get('api/ProfileStatus/Lookup', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetCuratorsLookup(self):
        self.client.get('api/UserProfiles/GetCuratorsLookup', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def FeatureFlags(self):
        self.client.get('api/FeatureFlags', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def countriesList(self):
        self.client.get('api/geo/countries', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def countriesDetails(self):
        self.client.get('api/geo/countries/PH', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def regions(self):
        self.client.get('api/geo/countries/PH/regions', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def cities(self):
        self.client.get('api/geo/countries/PH/region/PLW/cities', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def Candidates(self):
        self.client.get('api/Candidates/14800', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def Candidates(self):
        self.client.get('api/JobMatches/Candidate/14800', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetApplicationStatus(self):
        self.client.get('api/Candidates/GetApplicationStatus/14713', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetRemarks(self):
        self.client.post('api/Remarks/GetRemarks', data={'candidateId': 14800}, headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def QuickLinks(self):
        self.client.get('api/QuickLinks/Candidates/14800', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetRecruiterOfficeUseDetails(self):
        self.client.get('api/Candidates/GetRecruiterOfficeUseDetails/14800', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetRecruiterNotes(self):
        self.client.get('api/Candidates/GetRecruiterNotes/14800', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetEmailTemplateMergeFields(self):
        self.client.get('api/PipelineEmailTemplates/GetEmailTemplateMergeFields', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetActivePipelineEmailTemplateOptions(self):
        self.client.get('api/PipelineEmailTemplates/GetActivePipelineEmailTemplateOptions', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def ResumeTemplates(self):
        self.client.get('api/ResumeTemplates', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetApplicationStatus(self):
        self.client.get('api/Candidates/GetApplicationStatus/14800', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def ChangeLogs(self):
        self.client.get('api/Candidates/ChangeLogs/14800', headers={'Authorization': 'Bearer B-Ab5ZikCxFKrTOv8ex_WB-ubNowF8MMjHNKpUL_T3U2qGk0esQTbDDCLupciOAhIj77Xx6e42j3r1Ry_ZxFCfwB8H7okoLW1W_KODXG9LZBlBiDf5Vjkx0xJttIiXvbeZ9O1TtW5SPgX81bf3gZU7g-rkFCCJtGjKPsc-JWs-I8dKjjY8Wl0BHeRpbN_ZyxKimyCPziBREqM1K1GuTsqBuFLBgD4IPY96XP8AVxM4tRCzp8VTZwPUIQQrgHdKp7CoT9u-8XlMfLsmp1nm-6s4He_9693xiY_-h6ULHKfYEcQl4-Vh1SVD6CHc5E6mv7kBjRQpfaCdOvLqJ825PcXeQ9yp25ZgdkN7I7IereQdJETlp5-nYHYNVNTMc5vyUif8mXdod8NoRnDFFXzVUzgriOO3QQ2A9C1EGbq6F_g-KEJ-r8z_KWngKwaWjPeOEXuOV_5X3ao-Lc1fKSyUlj_TjoD9DrwHMemB2QUUmooA1JUGGyxAjdSLh1pTxKLD0CAINOWawkLfhqqEuNXBDxuHURenHIc7XNdsDaYsof0QRar1-rvY2XQlp6rl33Aym07iFx9rz3Mi5qi_oDF5X-L2iVRn6VR3hPDxSlkEynkwda2g1KrXGqfmwhWUEF5VBPpfwi2zoQWIfJjeWpZbLr0RKp1PvuLYX9XHJh-9ubEFQoJhWJbqtmKAU2kLx994U0drtvEl5v4lcmYVNuPTxLHgyb3FE2p-W2WrnZqyQd9l8y9rJWgHwX0QhrizNNkuxxYRN86jblHQcPYHBjmBFTnQ', 'Cache-control': 'disable', 'Cookie': 'abc'})

