from locust import HttpUser, between, task
class WebsiteUser(HttpUser):
    wait_time = between(0, 5)

    @task(1)
    def FeatureFlags_1(self):
        self.client.get('api/FeatureFlags/IsEnabled/4395', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetIdByOption(self):
        self.client.get('api/CategoryOptions/GetIdByOption?option=Replacement', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetRecruiterOptions(self):
        self.client.get('api/JobRequests/GetRecruiterOptions', headers={'Authorization': 'Bearer -UggKW9qN2A-DqKP3g1GQoyO43Yw8_wtbWxn8tUYTkehPhpI_R8TOvKKqOpSLlocIRWjb1hfxCs94D6bXnfr8ZELKBvdOAiWl8DK2kNcHy_D2vV1ttPl6GN7TbBQgTaYci68yHFNdDnSDhDnO_iwiXlG3O9ssKS0JaTxwR-RXyrIjgX96yOAig-zbNEpEaJZ2o05OvCrpqIG08onKyTbuMx2NscGOtInFmkIncsrBbVBxYyfCe93wVXOIgEhIXPm7zKOPW8ltBLf5RE2mZjUyFo8lRUQ8oE6_2_EuHxAAKsIx3E3X44JDUlJipEHndwOx2c1uoGTwfLdCE5KwhXM8r8znzlRvXfzKegOz4Z43Q9AJZkkatYiJ5i_ztEUm9_s38Sblvqywd1gr9yb9emxl_UDQJZMciN1HawZdRnMwFsLEhMVi_5g9fjQP2tsF4MN-k5_VHVnaYOAbUxlo7U76gguHeXKZhxBUowyDisetMruXh8ybBucVDaWjVJ2heII3VJdbi694N1UwGYejiCcLabP6zaXFrC-XWHKlu7hjxSRgUSRy_c4uIRIKKe609K5kNWBYAk-jN2sINQxhPd7xBXy6i1s-sS8TXMvQsuHczgMn5eTbaPozbMxpUAEDUFH-EdL5bhsKx24ztQdh3vc_FAGwAJE6oJ3aH_5-jqHVD5m7g1kTaYbXZWbxF3zh-AG1rj063VH6Dz3GXj9lQRtdOEhbxiZjP2Y7S5IdpYhIqrV5VoFq50EbfzZplI0ziy7wYy4IkKqwJdf3QZtgqk7jA', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetClients(self):
        self.client.get('api/Clients', headers={'Authorization': 'Bearer -UggKW9qN2A-DqKP3g1GQoyO43Yw8_wtbWxn8tUYTkehPhpI_R8TOvKKqOpSLlocIRWjb1hfxCs94D6bXnfr8ZELKBvdOAiWl8DK2kNcHy_D2vV1ttPl6GN7TbBQgTaYci68yHFNdDnSDhDnO_iwiXlG3O9ssKS0JaTxwR-RXyrIjgX96yOAig-zbNEpEaJZ2o05OvCrpqIG08onKyTbuMx2NscGOtInFmkIncsrBbVBxYyfCe93wVXOIgEhIXPm7zKOPW8ltBLf5RE2mZjUyFo8lRUQ8oE6_2_EuHxAAKsIx3E3X44JDUlJipEHndwOx2c1uoGTwfLdCE5KwhXM8r8znzlRvXfzKegOz4Z43Q9AJZkkatYiJ5i_ztEUm9_s38Sblvqywd1gr9yb9emxl_UDQJZMciN1HawZdRnMwFsLEhMVi_5g9fjQP2tsF4MN-k5_VHVnaYOAbUxlo7U76gguHeXKZhxBUowyDisetMruXh8ybBucVDaWjVJ2heII3VJdbi694N1UwGYejiCcLabP6zaXFrC-XWHKlu7hjxSRgUSRy_c4uIRIKKe609K5kNWBYAk-jN2sINQxhPd7xBXy6i1s-sS8TXMvQsuHczgMn5eTbaPozbMxpUAEDUFH-EdL5bhsKx24ztQdh3vc_FAGwAJE6oJ3aH_5-jqHVD5m7g1kTaYbXZWbxF3zh-AG1rj063VH6Dz3GXj9lQRtdOEhbxiZjP2Y7S5IdpYhIqrV5VoFq50EbfzZplI0ziy7wYy4IkKqwJdf3QZtgqk7jA', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def ManageLookups(self):
        self.client.get('api/ManageLookups', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetIdByOption(self):
        self.client.get('api/CategoryOptions/GetIdByOption?option=In-progress', headers={'Authorization': 'Bearer -UggKW9qN2A-DqKP3g1GQoyO43Yw8_wtbWxn8tUYTkehPhpI_R8TOvKKqOpSLlocIRWjb1hfxCs94D6bXnfr8ZELKBvdOAiWl8DK2kNcHy_D2vV1ttPl6GN7TbBQgTaYci68yHFNdDnSDhDnO_iwiXlG3O9ssKS0JaTxwR-RXyrIjgX96yOAig-zbNEpEaJZ2o05OvCrpqIG08onKyTbuMx2NscGOtInFmkIncsrBbVBxYyfCe93wVXOIgEhIXPm7zKOPW8ltBLf5RE2mZjUyFo8lRUQ8oE6_2_EuHxAAKsIx3E3X44JDUlJipEHndwOx2c1uoGTwfLdCE5KwhXM8r8znzlRvXfzKegOz4Z43Q9AJZkkatYiJ5i_ztEUm9_s38Sblvqywd1gr9yb9emxl_UDQJZMciN1HawZdRnMwFsLEhMVi_5g9fjQP2tsF4MN-k5_VHVnaYOAbUxlo7U76gguHeXKZhxBUowyDisetMruXh8ybBucVDaWjVJ2heII3VJdbi694N1UwGYejiCcLabP6zaXFrC-XWHKlu7hjxSRgUSRy_c4uIRIKKe609K5kNWBYAk-jN2sINQxhPd7xBXy6i1s-sS8TXMvQsuHczgMn5eTbaPozbMxpUAEDUFH-EdL5bhsKx24ztQdh3vc_FAGwAJE6oJ3aH_5-jqHVD5m7g1kTaYbXZWbxF3zh-AG1rj063VH6Dz3GXj9lQRtdOEhbxiZjP2Y7S5IdpYhIqrV5VoFq50EbfzZplI0ziy7wYy4IkKqwJdf3QZtgqk7jA', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetSourcerOptions(self):
        self.client.get('api/JobRequests/GetSourcerOptions', headers={'Authorization': 'Bearer -UggKW9qN2A-DqKP3g1GQoyO43Yw8_wtbWxn8tUYTkehPhpI_R8TOvKKqOpSLlocIRWjb1hfxCs94D6bXnfr8ZELKBvdOAiWl8DK2kNcHy_D2vV1ttPl6GN7TbBQgTaYci68yHFNdDnSDhDnO_iwiXlG3O9ssKS0JaTxwR-RXyrIjgX96yOAig-zbNEpEaJZ2o05OvCrpqIG08onKyTbuMx2NscGOtInFmkIncsrBbVBxYyfCe93wVXOIgEhIXPm7zKOPW8ltBLf5RE2mZjUyFo8lRUQ8oE6_2_EuHxAAKsIx3E3X44JDUlJipEHndwOx2c1uoGTwfLdCE5KwhXM8r8znzlRvXfzKegOz4Z43Q9AJZkkatYiJ5i_ztEUm9_s38Sblvqywd1gr9yb9emxl_UDQJZMciN1HawZdRnMwFsLEhMVi_5g9fjQP2tsF4MN-k5_VHVnaYOAbUxlo7U76gguHeXKZhxBUowyDisetMruXh8ybBucVDaWjVJ2heII3VJdbi694N1UwGYejiCcLabP6zaXFrC-XWHKlu7hjxSRgUSRy_c4uIRIKKe609K5kNWBYAk-jN2sINQxhPd7xBXy6i1s-sS8TXMvQsuHczgMn5eTbaPozbMxpUAEDUFH-EdL5bhsKx24ztQdh3vc_FAGwAJE6oJ3aH_5-jqHVD5m7g1kTaYbXZWbxF3zh-AG1rj063VH6Dz3GXj9lQRtdOEhbxiZjP2Y7S5IdpYhIqrV5VoFq50EbfzZplI0ziy7wYy4IkKqwJdf3QZtgqk7jA', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetAccountManagerOptions(self):
        self.client.get('api/JobRequests/GetAccountManagerOptions', headers={'Authorization': 'Bearer -UggKW9qN2A-DqKP3g1GQoyO43Yw8_wtbWxn8tUYTkehPhpI_R8TOvKKqOpSLlocIRWjb1hfxCs94D6bXnfr8ZELKBvdOAiWl8DK2kNcHy_D2vV1ttPl6GN7TbBQgTaYci68yHFNdDnSDhDnO_iwiXlG3O9ssKS0JaTxwR-RXyrIjgX96yOAig-zbNEpEaJZ2o05OvCrpqIG08onKyTbuMx2NscGOtInFmkIncsrBbVBxYyfCe93wVXOIgEhIXPm7zKOPW8ltBLf5RE2mZjUyFo8lRUQ8oE6_2_EuHxAAKsIx3E3X44JDUlJipEHndwOx2c1uoGTwfLdCE5KwhXM8r8znzlRvXfzKegOz4Z43Q9AJZkkatYiJ5i_ztEUm9_s38Sblvqywd1gr9yb9emxl_UDQJZMciN1HawZdRnMwFsLEhMVi_5g9fjQP2tsF4MN-k5_VHVnaYOAbUxlo7U76gguHeXKZhxBUowyDisetMruXh8ybBucVDaWjVJ2heII3VJdbi694N1UwGYejiCcLabP6zaXFrC-XWHKlu7hjxSRgUSRy_c4uIRIKKe609K5kNWBYAk-jN2sINQxhPd7xBXy6i1s-sS8TXMvQsuHczgMn5eTbaPozbMxpUAEDUFH-EdL5bhsKx24ztQdh3vc_FAGwAJE6oJ3aH_5-jqHVD5m7g1kTaYbXZWbxF3zh-AG1rj063VH6Dz3GXj9lQRtdOEhbxiZjP2Y7S5IdpYhIqrV5VoFq50EbfzZplI0ziy7wYy4IkKqwJdf3QZtgqk7jA', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetBDMOptions(self):
        self.client.get('api/JobRequests/GetBDMOptions', headers={'Authorization': 'Bearer -UggKW9qN2A-DqKP3g1GQoyO43Yw8_wtbWxn8tUYTkehPhpI_R8TOvKKqOpSLlocIRWjb1hfxCs94D6bXnfr8ZELKBvdOAiWl8DK2kNcHy_D2vV1ttPl6GN7TbBQgTaYci68yHFNdDnSDhDnO_iwiXlG3O9ssKS0JaTxwR-RXyrIjgX96yOAig-zbNEpEaJZ2o05OvCrpqIG08onKyTbuMx2NscGOtInFmkIncsrBbVBxYyfCe93wVXOIgEhIXPm7zKOPW8ltBLf5RE2mZjUyFo8lRUQ8oE6_2_EuHxAAKsIx3E3X44JDUlJipEHndwOx2c1uoGTwfLdCE5KwhXM8r8znzlRvXfzKegOz4Z43Q9AJZkkatYiJ5i_ztEUm9_s38Sblvqywd1gr9yb9emxl_UDQJZMciN1HawZdRnMwFsLEhMVi_5g9fjQP2tsF4MN-k5_VHVnaYOAbUxlo7U76gguHeXKZhxBUowyDisetMruXh8ybBucVDaWjVJ2heII3VJdbi694N1UwGYejiCcLabP6zaXFrC-XWHKlu7hjxSRgUSRy_c4uIRIKKe609K5kNWBYAk-jN2sINQxhPd7xBXy6i1s-sS8TXMvQsuHczgMn5eTbaPozbMxpUAEDUFH-EdL5bhsKx24ztQdh3vc_FAGwAJE6oJ3aH_5-jqHVD5m7g1kTaYbXZWbxF3zh-AG1rj063VH6Dz3GXj9lQRtdOEhbxiZjP2Y7S5IdpYhIqrV5VoFq50EbfzZplI0ziy7wYy4IkKqwJdf3QZtgqk7jA', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def Pipelines(self):
        self.client.get('api/Pipelines', headers={'Authorization': 'Bearer -UggKW9qN2A-DqKP3g1GQoyO43Yw8_wtbWxn8tUYTkehPhpI_R8TOvKKqOpSLlocIRWjb1hfxCs94D6bXnfr8ZELKBvdOAiWl8DK2kNcHy_D2vV1ttPl6GN7TbBQgTaYci68yHFNdDnSDhDnO_iwiXlG3O9ssKS0JaTxwR-RXyrIjgX96yOAig-zbNEpEaJZ2o05OvCrpqIG08onKyTbuMx2NscGOtInFmkIncsrBbVBxYyfCe93wVXOIgEhIXPm7zKOPW8ltBLf5RE2mZjUyFo8lRUQ8oE6_2_EuHxAAKsIx3E3X44JDUlJipEHndwOx2c1uoGTwfLdCE5KwhXM8r8znzlRvXfzKegOz4Z43Q9AJZkkatYiJ5i_ztEUm9_s38Sblvqywd1gr9yb9emxl_UDQJZMciN1HawZdRnMwFsLEhMVi_5g9fjQP2tsF4MN-k5_VHVnaYOAbUxlo7U76gguHeXKZhxBUowyDisetMruXh8ybBucVDaWjVJ2heII3VJdbi694N1UwGYejiCcLabP6zaXFrC-XWHKlu7hjxSRgUSRy_c4uIRIKKe609K5kNWBYAk-jN2sINQxhPd7xBXy6i1s-sS8TXMvQsuHczgMn5eTbaPozbMxpUAEDUFH-EdL5bhsKx24ztQdh3vc_FAGwAJE6oJ3aH_5-jqHVD5m7g1kTaYbXZWbxF3zh-AG1rj063VH6Dz3GXj9lQRtdOEhbxiZjP2Y7S5IdpYhIqrV5VoFq50EbfzZplI0ziy7wYy4IkKqwJdf3QZtgqk7jA', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def GetSpecificIcons(self):
        self.client.get('api/Icons/GetSpecificIcons', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def FeatureFlags_1(self):
        self.client.get('api/FeatureFlags/IsEnabled/5188', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def JobMatches(self):
        self.client.get('api/JobMatches', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def JobMatches(self):
        self.client.get('api/JobMatches/JobRequest/0', headers={'Authorization': 'Bearer -UggKW9qN2A-DqKP3g1GQoyO43Yw8_wtbWxn8tUYTkehPhpI_R8TOvKKqOpSLlocIRWjb1hfxCs94D6bXnfr8ZELKBvdOAiWl8DK2kNcHy_D2vV1ttPl6GN7TbBQgTaYci68yHFNdDnSDhDnO_iwiXlG3O9ssKS0JaTxwR-RXyrIjgX96yOAig-zbNEpEaJZ2o05OvCrpqIG08onKyTbuMx2NscGOtInFmkIncsrBbVBxYyfCe93wVXOIgEhIXPm7zKOPW8ltBLf5RE2mZjUyFo8lRUQ8oE6_2_EuHxAAKsIx3E3X44JDUlJipEHndwOx2c1uoGTwfLdCE5KwhXM8r8znzlRvXfzKegOz4Z43Q9AJZkkatYiJ5i_ztEUm9_s38Sblvqywd1gr9yb9emxl_UDQJZMciN1HawZdRnMwFsLEhMVi_5g9fjQP2tsF4MN-k5_VHVnaYOAbUxlo7U76gguHeXKZhxBUowyDisetMruXh8ybBucVDaWjVJ2heII3VJdbi694N1UwGYejiCcLabP6zaXFrC-XWHKlu7hjxSRgUSRy_c4uIRIKKe609K5kNWBYAk-jN2sINQxhPd7xBXy6i1s-sS8TXMvQsuHczgMn5eTbaPozbMxpUAEDUFH-EdL5bhsKx24ztQdh3vc_FAGwAJE6oJ3aH_5-jqHVD5m7g1kTaYbXZWbxF3zh-AG1rj063VH6Dz3GXj9lQRtdOEhbxiZjP2Y7S5IdpYhIqrV5VoFq50EbfzZplI0ziy7wYy4IkKqwJdf3QZtgqk7jA', 'Cache-control': 'disable', 'Cookie': 'abc'})

