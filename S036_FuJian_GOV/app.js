/*
@File               : app.js
@Project            : S036_FuJian_GOV
@CreateTime         : 2023/3/15 22:22
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/15 22:22 
@Version            : 1.0
@Description        : None
*/

const CryptoJS = require('crypto-js')

function b(t) {
    var e = CryptoJS.enc.Utf8.parse('BE45D593014E4A4EB4449737660876CE')//r["c"])
        , n = CryptoJS.enc.Utf8.parse('A8909931867B0425') //r["b"])
        , a = CryptoJS.AES.decrypt(t, e, {
        iv: n,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return a.toString(CryptoJS.enc.Utf8)
}

function decrypt(data) {
    return JSON.parse(b(data))
}

const data = "N1jfMuHUNZzAwf7B5RzFD518L/PWAvvVi18QoEWnsY9M70Xik6ShsNyLqEBziJu1nQQn7I0VJ0mwcSYFJ8IzYAH+208ailwfpnssL8eR+VX8Msph+r169injWQXxsGm+O+I90hXODVYNtwBPsdM72maLtMETQ14MKI6PZmVeJxGs/OE296XSguQGcv0CMlvsGqrr9amF6+4yo3k2O4VExSzpHQxlGWL3lG90X9FdRlPMpSApixySyDj+sE3JmYy6qx6VgrRUSJgx/UU9BHp54oIXjkzEmbnQLz3+jEjwfSSWKyVNuSuA6LIbWGYi6cYzb31iO8JfYab7wvv8m32xzDqUO6NK6k9Jk5lyl6ORBSrynWWYZGSxxVRzIAWmNoDRkgoa4+pjN72JptJKzJjz6vSFPUeUTQGlE5QfVvkOAspgr79XnoemCJpkPpGHGUqpZ4I4HDfYicVmYXIwi9NqrKHNJeX3R7mY9wQ4uNBkD80Ng6yhAmxczjMSHKzM7CULaw66pIT7llClfMOgwUigCsRMcl7D6QafUZ9yDMcPcldQgVJyqEe1/VpTYMTfpcqdSH8ryJ4G95egW0GSu87CcpctwfNIt59bHX5nv/6RV4pJoupHJYo5Dgszy0EIykw9hr3ce/QfbloRICN6QwZ1qg/OeJTXa16Dl8wJMoTzERg0nRMd74dNkTbbaKUblY6NikMuiPvTYC8rcbY3kkJN5prtD4HhkLxMGzaKhTbHW8KWanILDsiGABaWCtLurj4/IuqeIckYjc4SI0QZoxsy8DBOUYVMxXryd4hhwlu34QF/42BEMA4MBrNUGGdFNtTrXSbrPoSC76bVFpZ5LiCqqk7xCq5YAhoDP2mHcH2qfe6kCr+oJUn9oRkG54+L8FGe4ipXk4MEcQzWaiQQWEWFH5w343cKg/HRxQdz6pHcVRO4av+YsQA2BqR29D2DwVGJf0bQXMqZeHFW2+xgL5oDrY5X/K15BvmiCpdg5CIjsxq6WxQ1hAKKGni3QW3bQOAtU8D86mUnZSlLfa8vsbljtiNGOf4EH8jpHDrB5hW+Bi/uWQs3BSHs/QxW0aWfsnoKaaVGqwP7nl7O2OHQvI2BjQqJADJzsiM51ua+b5lXBkHF2m7QQ/fQhNF9XX3RkdprK9zWx/kAJMVn1Cqzk+cxWo7rLDBIYnhTk6UzbMP1VxsU0NRFUFiwwmumPR9pw5Q5BTw+UjP25E/T4aLAVJkC/vixsorFzjGEnF26PEqfrMgokIfFJpIAwyGPPLGNlNvMHLitxzc5m4j+ph0PS4IcUJ/zQP+xN5I1P3ukGLzqwhZ12Ue1VtOmH7/ep6o4RAJGkBAvA9MWR6GnUd2aqLbUEqRKMygWWW37ndDeTBAD12gxmN8QOtmlSA5zvezQumqAU2bnPd7J6vU8WaJ610zMFLtZ0hAlcb+hgKWptpm9w3XmznBWTlj4gc2z8bIPwrSO76QCno72Jw1YZXpJxgzGAvtId/JqMvKsBiOVYOX1pPJEp6CdXVUSIMWGZjOEklRaO5t5ugQM5nS44zrh9ySPmBaP2ogwZrjqND2CW2ypqvoiecS7sTyb7OL34BrWGDLCwn/ySwHfF19AM8Tty8xgUOH4UGL0AreSzG0Gc1uJ5YJ10psRZOR8dNWG0UOH3t3Av1wZbQQtZPaM5unXzI42RLhAhXTLEfbS0bE6rfsSBwpUixl+Ybdgh0mRu5O6DCVoafx8PuSdSoiTri6yEzLKcSDwGG5phHssVVIlafjIvvoSzEcIR0fuhBCTSPT/03NTwcW6bxKeBmczXjKS1pjubMIR+TmxsSlNzpSJ7s3GS0AXPTXTJCgxskaiuOIw0X+5HE6DPzjtnSxA+Zt5AJl/y9RqmTQS5x9RCEl4Sozouclx0ulsdm0/WtDnehMEhXBKJH+tHx61QDLw3i1Rwz5k79xKmOPhRzeHSlTYQ0Vxj/mH0ETsBPjrj8aOjQDxep5co+VfkRKVwWwe+0/N6nicVlOI4odDMBSY6jJOfsUUsxohrPhC2zIOtN40jgZnumjHJU8QY+mIM9a3/I62VGmiC/tooj/IceOMfbWiFZ5UVa/0S9wNdufkBzJ6wKYFavVzZPV/4MqMtSaaelosBjFR4cSRdETftRuByswyXm5rKMYrb1U+vRkVwKeyFYjzkCQo/sGfieYxRp4FxGeu4Xy8PspVvDpmJp4dHsVIzVcLEzt4P0xschGa8tKEg/ILPcdx3mnTYSVQac4poVbSOw4w2iFXi5nrarsAWSdrYo9jH371F/LYZxJn+64DGVZQE5Dc9Sr9A67RycH6Wc4c8dnzJsvmBA9tdMSJbxxLlvrI74M2ZJgq85FvEcRWXMeyojZqYpWUo509hP/TkshjHk8X78ukcvsCYANDwMF5+vIt8zpsKdPa64f2PUtyutkTS/zbZnVwAKHaW6fMrgZZMxDDB1R61fhoVy6dgWp9mJyrf6Xkj2HPo4JAI6zXG3BMc0TESIiArv0Yvi94vCxEl9daVDizlebtfSRSQKPMKYONYc7skiyI0bP7PgRb3k1GlJZa5EnORsScPO91WHB97wd3QiKpxMrcV6tGeclp/5wCRwoRQlRufOzgV133xw9/tYyOT7vkC6Wp4V6V4+JRAcK4y11P7ZIYjAwuTlphu8no8vQNvpDL3mgyiYKq8hAY5xU0e2sWfQhT+hc9qknCoQJ9BT1Wr/66UN9H9ypzczdD+0rH9m7pxgFiyPZa5MWH8G0b4+xiInOkPDqeQTsVNBD4a79KHnYZbu4fyibKhMVur7YiYiJxL/9Q8+RD584/aRcei8Z9YM61P907+fCXoHFm4uPipLERygS92PJ4O4hu4wvIGHnhw5Gnm0vC0QQu0gITYuRXE8eEm5ahEFqYeWtblON2NkLgnkoR21Y2hWsq51Z6euxCXDyMMbqI+GC3weIoZgEBD1U7R+Di2EBtdvlIJ24Z9uCDr4fKBQteLvV2na+K5lP5MWsUL+TEfUoyZyfrpao/zioEdsAV9nPlCTkmXjsO0jTwGjoLERF7Sjuf20pD+3r3KUigIZ8s+BB7ghDbCcjUOScbJkLCCjzId2JqN4VAhlslLtIx5w35rs2/Ruud1rd1SWWu5A8+Dr27ACb9zuH1Tz/2Sb97k+l0X5AmjSAsF0tGr5HEkWNrvnNYHUckSkO4qzk7c2srm5oeNld4kbm3qlyFwKNxFOC5W+1DYLMmvwQ1VQNTGzorDuvVAO3bpIG6Ts96w6wTFLuMzwFGZMT+ZIA0wUwR6cLBNfTU3fAFlFr6JN+T3sDWDrUwUGb4jLhUSJLYx6UXm7MUi2Vwdy3ok2Ohi4UdMHldP/e+j2RhFb8M9GWcePQKUs7igURN/RF1Tv6L5b53IGqeEWaVcJaJGYg5xRw8vauXgBEIBy9SbQRVh2ocy2d6yhlc4FNQ0DCd8+DCuw7fm3SQYr55pIcECN+64qxT4OmHiZ+aqenrowl5a42Y7+sRkiEGuhEcXgCReB2zyYYNSwx0PF5pCYUYmBIXe7jbGt7rMYQcvQhxxh8x9Bwu1ZHPp8+0rsQiBzwFZG6wp67ew++irFK5+nh+Yd+bcByftAJiJYc2PcwBUHv4EPmHbBC9Ghl3VSH7SO0rpRZTslrHrjp+8l9UjzLq3sDCByQdnVWLNQRpTdE0rEgz2jRW2apC0Nog+SaCMmCjV/qAgO79lZ0jLJwGXypo9Gm3f7DjGT1IAzSjXbexZ0E4FfFxiHcF24msgdgnonVdvX6YW8GUZEQuA9Rjs4XYc01uXTefQPGMGLctCKzPDcfvuUHYzAtFdIbp2NXbYay/J/Op0yWv+4JPm2jAfIK8DVHR/ifM4Qd5LxZkbUSpzLBfu/WaRT1WFoD4Dvqsar75xIqRR+ytQ6jcC4XzaHZ9dwmk89QX9s/4xorgCQ9ki+5/7sIv0mh/4UYMRJwD4/n9uwy2M8OtVnAhuoXtw2Z/fMA3xLu9BlJQsD3iEkTGXcrQ+UYsAsgZrqmptzvdb7r4wUIsSH/Tlu7+ofdYeDx2xsWKTpb4tfhTMrwTvVZyYr33h2kOEqSIV9oG1zx0WLdI6p36vDfQDLyMMYz/zCj9BxHG3pf9jEcXyBLhzM0T0NyQdS+z4iWP4/CoCJq9ne2kf92srQj8IdwPlIp/8qbU3Ttb057geeBUve0J8/F3VsOSdjWK86p8d6vL8OMX6Y/edDIaamu1FdjbfQi0kAez/HDEZyh1X0qbzq+ho5s6bJhSvjCpY4Ux7+yXGDSTTwoANA8dgPui+QD+wPzijDwy+TftKmTA6OCzkYDVp8TkePvfWV977g2QrDMnx/6ycHHrFe5jBuRJQiTT68SsLyS/t8S5Gta7HPttjjMgk9DsSXfFdVYLF1XNJQaxU4MrNbpJM1u3OiO2qn3F4z/vdqNx5Eyj+9lh2+20MYTNsPo2YVcL8FSG+kUCCwvmvAMqjaiRgwQ/H2oVqAs6B6nSkWhmObj54uHut5oxTwo1IzAI9KVNn11uggYsyYznbOAOz6iYmQwWNA86skaHwfI4ALeIPFcoUApXx5upxlvY9GBhfKqahG1NdtJ4unp58rZYAK+cg3QLtPnmuu5XYtsPOV84qrgq7688etci54PNfMLkBHYZK26bWxTmIt2QwEAn1yuIhhSyIsY7Ns2DBpqVyC9IQfwYCKglNNzZz67TE3DvpThSoB3dY7OW7KyjJ9x55/CTA3uc4qNk5/SQlSAjxdCKgidTdMDLinxHZlLAhwCKR8O7x0wjxCm+1Dsmfa7AbMpF6p9j4WwXRKhDKPt5sEds2P6LjjGr8NQeVNAQp6PNOekO04FjgjOKbHKN6l3iB267fsGDlMRs5a+likReuIQW6X+7KOD4oxDYDyCksbuLVZlMFS9a2bjUmDLOAui4m3s8WikK743pZ5TAbjgAvva13lrOet6Uav0Z3c8+USfxtAjzjUMPkX9IHYGBYwX/uw9J/C4qiaNQjveNkYYJYS0TLnperdmK7Dfr59XbeldCwTld9QgElVMR1uudm95QY7FFIpftJ9NCsWCpkPu32l1TaO5jRWe9SkXHDUd6XkqDpLvf8l1jj+hNU6K2HFiVCQnuH1+udfudTFeREmN/zzwd0CKVu/mgJVBtzlEtL+qfVfCSakux+KPSapKJaHsg/SafNysC2vrVlxj5c4Edz01SZcTBw15dH4M5FAFC18Vj4GlDaVgpFB+jIuQWT0/rTzaMK0s3bTKG+8PotCHfokWDEET3cHNs7fx4YKmok/q0G/QaQE/oy62HPq7q6bTFEHdLSlzULH2M1mW0LJI5KVFnONwM1elxR6am4n+egfQhEe83k/eVl9uBxIB2Zp+F7+JtcQUAuuahyzgtlYPIjDBs0aEfQtBAzIlhpI/VXA2VoXUtbaI2JTP7i7wJbFLNJL5nGvFfMDCpRBJIU3VBThjp8QYgiCZtRWxIs3XwnvCplhu25MjynuZy6LF+ZpxomRD/Y8aG0UhN+CPxsux8hwBTg/qduPAkDRnAN9/99LRYeKbu64LGPazXTaZSfRXlDVqqYuF2deQ3YnzSKeeNu+L62JtDaBi0RddN8josjHky9EvOGOJcpTq21Ye94nbxzp1MrQKp8HMiGAjLcuPsOK5w4AEpsZj4bjLb9Rvq+vBBv+Q9amZzEBlG4A/OMg9y0NcHCAvujfK5gilUvXckNoxW6QGBIn09L4RNTIEyJwQhUVYSQnbw5vl9HQwOsgLOqcvoMHUPAbLm7DxQskWr3cFaJaEnrFZeycxh9AXzfqx4C1pukBxmNBXYuY4I6dT7nNtiZR9ZrFR4sVhb/IlkSVF2Bt9g683lsAYm8FByM+zDDta+AYkQItgGCEmoyOZH6yoDfVl/q3gU9Jo94T+0U4prlQdF+qonoFFkFJdWfOSBjvJOYDsJxKBNkSNE8xca6RwDXJr7JPyKRUkdd8zQzG6DKqPTTtYC+Ocuhb5LudQrPTthboTO3z+ve0FaX0JODA3/QrpyfX0+0ANyhRoqpvEMHYDeVKd0y0jTzG+X/gcatOeQlh9gblOaLd8WLRHzUF8jDHXW7mSd0UlC+wDNHxXFnXXsWwhFyafDSnOpRbowyGCUjeT4+Qzo2Omvt/N0zUFQ10ixDENVRMgpqjpmXDROPpeV57f06Soez+7jDep41MQHHmQf0gL01us1CGkVb6bXpS4Gah/dwZUv71nfMskCv/9EvYnrEqGPYCcZdI698DDEd93IOsKRZJEzlvaohIzfGjjVhxGoItULckOHpr/5oa0SCC/bMBhuK4b3CiASJyJJAwgoAN0scDHVkP/0FLMSOyoN3Obv83LUv4Qm8LcL8uuMCf4gcdv8+tqugrh/g/+HhDYT0BAcb+7eEPewroUp7PQ7QLkfWc5DYcu1pZ8RM0wnPQ4bTfAaIBu/oaLL152xP2cGKKp+5Dyp7sopAL/c4m+MOZlp+spfa2XWR3gBPi1EfJ3/slB93B67nfNrpdMS6qZ1D4PWCht75KjSIREJyBxPHrF8xK0g+SYIWlrtb86LhCslpL2HhK73SMMJgakQbQ3iCCulwaOF5GFy4Bln62FzSyqo2MP7/GBjk1Lva2V3TwvLH8qjq9MnlYNxz+/uTfiM3Oxj/l0u2HhZ9PwQiXsS+oFx0TzypDr400Yjr2iCaENNDMSiHIOtPPQxDcrwbLZEUsDkHnFZNAjPUuRFmSukTXWhUaGcMrplpqnuL5N3yY0Ik4gRvebCO/kLSPMEdeWv7JjC7bzeLqs1j6rkpKu/JqgLAMUCN5626L0sm8iOj+ba6Cq4K7TY5TBlRrsRp0NPhz5fEQdl0k6sJrLrerI1VvAGDDvJ+vGWWfANET8WAQ7gQkfzZ5CoaEPfixKYHM13VaMkXxOdImJb6QRZMOWN+NfjvZ8AMMQIjNmO1sNxo4uUqKL3fzE0HFeiGbpyxPgnaUK6GwLiqwEjRUGoIdKdEOav/zCGvXgIocFBGGu76/ftPE0k+pPyMtjlrCMtOY5AJe2C9Jm5ixPPlVPdSZk8CoJgX8po9IccD2KsaRYX7GjBAwyaik2N+uCYl2GUOpJ1MDoRoIqd2TawZercDE48gHEAcJYoeMdFlX42ZNzWeqRClVFstuY1RExsKV/Kmh+nIZ+LzZ2KO6MpzE/ZajaRKwrPJJ/La2sNWKAg/nf3FMmzLHO/d+j5KbQD4a3Wnx1FuwSmsfWnIEeBmFu0qeZe/ZXXUYiWe4WcPGH5Hz2ev6DW/leP8QYTvhavh0h8bjpf0L5/1WaMQzG+hKrgL8AjqUXmL34blrd0vSWjYBMh/Qs0Y6OtTs8KuqwgbolThF1QiH1cllj+Ghyq3IIyL8Ka93Kyp3Y5iG1rgkCfbGRpxvJVnIQt82b2qatQEgltr/5tPjt8+WnVzf2YoU+D6rT+tzNNXSQPXxz5X+ZVTXtyznTvMZwtgISmg9bjS1fzLru95Q2Tdkxb6Sf206sZ2hgBi4d1OXlvRaCgX5ERxVCzub3LGBrPECdu2Tk5k1W5OiIFJgUyUrimrom9LxpKoLkAqkfmVcTlGw1gMJQwjIJOZe1TuaNdd20TCp9vkIdUYWT5zAhxTtJzLUhKIvFMyLNmPkJJla5rf/VRlpDyi8OBuZ+SZwTcWUuiq3TwN+GPnx5P5bLAXm95SkOk0TxvXCLaGaoKuJ4mGBc4VzOFtRspMaHVwDBcZNlusUzrPxUcUXCF/29GFlPFlxhc0M1qMEWITHknFuErmhsHyHYMEhLH9LCOXNaZcvcdjFGKJ9mAGHV36ti6fRqDg6D/vSUpEOCV0wUvJdNqZ0gXsDnBqUF2emfLzF9lKB0+86H5dhKuTZxLZw/5KK7KrAa3bTO3Ivs6j77+kBLcJZ9nXELiEv7JrnBnkj49Pqc8nrsLX4ln8RE2Ro1CvBcKwtXDLhHlcpiokZ5Ko0v5av5tFPkdrRW8fFL6uTx0bK2zCKOljp7EWqBlKjV5KkvVfhbndFvK4yUDgUPFmykYdoZ77i9neYyAkvYpPEJmKghMq7zPoQVDU59D6bHY9qqQaFjKL0qva/z/y34EWikVdwjkAfzEDY1eya4/JuA5v8+lav9C/gh32xlVj8CC3vqBod8cyTfkhD9KKgXxe+uBR3+rA+FtT538XOgnoEB6i84KCLRVjIyYkuxUnVvghA4pAsLxF+kquDT/QdJZvjw4c3oGSS4GMuoGB5Js0vAFtIwwo4CJZrqlsPdjQGT7W4TZnNorasa3CsqOnvtjCfKCpLnmVpxdSlJh0ZRMKl/i+YUzMkr3JPJn5fqOUqrfzRsaMSKCZTiSj5K5UeJc/10RnCE0XjBrTlYaiVxGGJiIqkJfJC+sSo7V/Oo5OWJhhfwoF0GmFxUP5UY+fNDwKiO46JJre9cFNHuF0s1kLHiII67ab0NRb99om0/KAkpIEa0P6du1b1qTF3itvmk4ueNz4Y6VZ55KJrQqWWgfaQdiOhxkKqwqRfpMnpjqJqe5sPPNnQvx4nTc1zkEYsXozRuS0c6YFhor/j6hD2hJCIzU/4MLoRDXimmAbsZcVL/SBegj61syNOBrrlXWbIteNbup50BxDCiRCgl/B8i6w1RC+eERaOLqxM4i6m8AGeYOOBjRLsycm1Efwpbh1HkUwBKs6HGSWxKWyek80ZNu44G/kwC4gTwzZlMn2L6Te5CZSeTMFkFsS+OdVhZ0Jf5CTXfllpw5Duvk0CRN60/55xl4rUOKltp5lrJ1gjioZn8niFlwXb6Jy88jZ4kqmZs6l/SquFTjh1kP21OqqCW1PbKQ6yLuxWO5eF4k6dRjgeeGkQ/bY9vuJTAHVZEj3aBE859v8zjo1ZI/WnlFTdr2gWfwPL2BLCfdxGsSzD/orBruvjDaTZ72DaZtAzTiuWPaJFXcuQs5N8/pDiz2sxpn2iXGMP3eNByu17WmL5hQAmDeHC3+jcAvlYFhcE9sRjUll3h63iUgksJNyMVHMRujzzP5/ABnXdcwDWsyxjCjlCZ0UblA7DVxnt6btoy1hsPIw9aYrGRIcWKAhpSJe2zCz9iWGiwQm7qnuqof+kGZqemYw3r56gtvourTtvvAXBbwk2so3Zl/YZu7WDJXs5e/UR9vPFBzVStPHjDQJvqINQmtCW7T62gKjAn8Pybdv7Msleb20Hitf+/7XKYgsn9QzQeVZBK75BBkBg6Q5qbYRlOBrI4F/iCHnFH429FtdJTnb7eFXbOTsusZhQ4u0p0nd8B1JXiw7y7RPFTcmlWWjy8vo7/fR1Pw6BeD2H2/GyU7uFvd1Gd4uVpjp1UUUJXuRvMGbHUZGcQGooy+fM2KRGvbOnK1mBe4i6Otfyb2xHxNV8PcoA2PKXBh4DlyBQ2rWWnTxjzeET34V3TKleA4jr7/RsCA0zuJNI6AZ7lNr/nfGUo/T9MYcPL8BqGUfrwS0UCwOSTbZdRkq/kf+u8OmnLWAd4PR5KsdRUIWKvBs/ZBbBCwB5Pp28ZNvVI1a5+Fm3TUsx42WF5G/72gpIOPbFksBRZxhIobqURVYp2zFoYEJfb4AHjqIHmvVR93Zzt2jXsJsoTeacuEw0ZrpHSlR4XP/r76SAbCahgvuX8VgXoyr8UG5m1YN2EC8jQy/DjBzsy5+afkLW4rwOZc7jnntmSEwcq5+KWp1zueFBuO+FfZosHqijKWZkz7kEsEc2wVMkjVf+sKyOVbUuZf31FHR2XdZzYv1zD09J1bvuayxg+snxbJzoezKfoUJVWOSGo4B9tdEh4f8WF/SQL1tmPPuG7W8v70/R1s3ddVb0giR4qzwbzgJ1jfIf+Y3nmu1mGXJc4zU9+gXOUbPgRYrtT0OOg6o8UQg/uRERDoCcyaT04ZI3oN3aPSyMZyKsMhK8XwbClmi0inpCuMb3NkqpRyoutAooS+aFo28isO3A8Vgk8OnwcIRlfTEZ+cUKeyhwlwxVWq05gpY3LfJmF+v3leBvZnMdJBR8Q6rdBTh5vm4wO7p62FfMieGHgvrkm7QAkuFupBUkfamnplp+6XqWpbP2j1kbUGvPsHnRZ/4qWHM3pYR6WJ8Ee4CN04E8V70hKzSD3x2gt+vlJGmz0G/qeOfOL66z0AjaI0JUBu8O7ZLhlCJCMB41eSBs8LoT2Jwr2fHjZqh9FDAoFACBsm2avEy+Mhkly+zWNb+tvZSCbgBddf3IFOFZ+qVnw1QBbdMcr4A5ecdU1OIUJ3rifyxZRyag+CecZqB89fiaeuUblaFNay581/cH3A+fQLMGeNAZ1FkAh57e4wWu1Mvid1QRFSHZyYYi0awHoSRkqXHZOaHjUBOIqZ1G2iCVjvGlxbM4hd5f5ZyezHNhAZyrp8hqAwas1yCYp57qSB+b3zIF5e1Vp16FWIzdQ/3sdmSI6m+tNmpKpe1EEF0Eb0U8rHPRZ62Y74bqCk9WRi5+WdfPxLlod4EJ2XNhWzuwrxm++NR+MrR2ltv1mFmuXqcSy3WxuxKaQAmIIFK9EqepFX8rgzRUVYGiMhEpS42o8CXpsLU1ewci9j8X0jqx1n3isjadW9zxw0GEPrE2dUHwpUg+YgYzTJZyZKjV3CFNXs+wfmuc+rk0JArDcyjalxW/oYV/6uqifBomVHjbs7uSF4eoRNb9sM6V24JKjlD0/H13asMGB9+Q266VtZaco3czH87GV7OS2Ugn0NBfUHF5M/gGN2TJMfDgkgGxcGgv03+FkkbGY9YK7tBHxPUJtC/Gfer0HI7uKvtgh9Q66ClTrnXCRlO+3+blVO8HBRzjQbUMQ+szjYebUhAaqn+qoCZ4ab7h3AImJPLyaIBDctf8flygDf9d8lFdoh5IpIR0BB8pN29v/VyXtmQ2ZIOj55d5St47tcD41VzbFm4efginCEOBkevG3Mx5TiN0qIRJeR+ANNln+Y/HK9M8h+CJP7tUvFod0JV31jFjLZiG6StTfnhCRazXW0l/4voguaFld0gnNERZRvD28CbM8BzMrC4Y03teK5k+80fSXqNmJBEzSLiZGVSp3HXdUhaAPx7eJTGFV12F1WV5ktIKCfyDr12YQ8qzOg221V8fg8HGZbMeMT7ix3IaJds8RHTlAiG9Rj4t7jPQytjLkQgntAcrmtcuZbyREyhsEUjfhYuu2lIdOm08yFD/GcXLUWjXZdjqprMbEnU7yflOxtOmJ8KEeUZGjBnU05C3N0FKJn/XCArVuiUCDbukUzlqhuvbGg0YB7Em7UIUz1epMEFaGTPFmycOSphUxJTdwUNQUdCON1Cp9DqdPY1oKqKh+jyzuY1mLFblxvHCx6/A9nuGGPHkys9jvfi+IK8Pvp6q++dqVwevm9Tv1uT5IArPzgvLpJ0PSJB3cRTBmWnj04Aq1bNeA2jzKxCfycjeWXuytGF5Z68vmb+20omKicaQzNL02e3m/Hg2zAS/BpVS6XfhueeR9BbTMwEd5mvdYr8yNTHXQJbmyZIAH2oxDvggf4PgAVuqrexP7Rg0ddORCTqZKvrSOW6xd/PdIcNcbuWxvFHCs8gI/WGXsvsR7zUPrhgLcjfv0PTS7cjU+S701F+JMnNkt2oVuDuXLP8ItbN9cC3wyMYvlBq/Av0xGyn8HfyTArbwbK3WJHLKHsZDaFagm5DIerfXXKfRMWfSYkp5OI7xuVuOmUnF9QU+LjqbtnYDI2l0JM5hqmV29fH3zP9/fcgjp+Ta5Z7RIMSY6FuFFsE36pQeOIubPkSCVznC76deDksq2/BKW+n6mazkMteMhDVrhBOX+nCNkS5IXuBiL2yjFY1T3t+3b/bZvLvKRxldIooppGNK29jD/RyyR79/fBlBNOxW4BzZaTO3sV+qg1ixRX1U4ucHgbdCHUiwTR7NBaZGBLKsi3cb0BoXNeRMUCrnFkkrx/FY41kT9/jdp7lgC+XwkFEvTFFX3XwNhVLpDijNlTXt37tDo3QJywibkJ6SwzAHAovA+iOOddc3qgVv+a3J30B0k2AseiJs5JKnzsphtqq/UH3yWHhg88FXRkklsiDlt4JsQVFnfEX2hGkaLpOMhfhHHXXmvOzEarTUEnxJAgoYISHQIPQhuaIVmTEnn/OgEopV+ahcEMeDeH9I04neALoI/6GU79e22PimK2ELS2FjDvL7V+MUYTxjr5BLXbOsC8C4UlwLP+kPmgJd6TqpGm4XTQ7lqy/6M6i4C0qHSNmsmVAMFmZOHj1mv503nirdE/Ruh6aEWVpk1GXVwZvC3zE9A6N8S1Vj9nWTccFny/03ZAHXC5ob/n3HtgDYy/Mw7ztZX9C2AX8qZVT+T5lTtbe0f27Q1sZvTopPeDdnsP32mbsf5xmdG/Ji53q0bNVERKJSRq18BMQa/aAGnUeik1up0ElQRqGbonobzNZpjZnYNyw/gtgtG79CiAwqv1TmtgwQmjvtA1qIv/H7l/i4hz1svM6BZ+uyRKTCA3dMvLAN0O9kl5Eqcto4NmkI0XlPquJngaB/pUDvKkFqrOAbqZna3MRJ4AY8/bQ+9fWtqSFXsYlLMip2L3gXk1GvBKvm94kvH9DEfssw/NsVIkxfiUrNG8jWm2RFdnNoS0Y8p1hdQqG/y5HeSPpdYqK5NwVCknXdMY7vkzF/GOjVAzHqWdZiJDBdbwRHTlzBvontycmsSZw82wVY6eREDKZhn5A5xnchqknZW7v48yC5EP6rNq/PeONrcjxzbNN8wzgfdyQVblgJGhbiK/slDFijiGDgQYL5lfDqOjh7iidHGrAKVbTQka4mikTkaPUfTgdN8JjWonnSjBmun/J2FDnQ5PbId2nkFX9AO3v5gWC++kTZi1w8DbjCPwEqlSTTqOOZxxnNcAKlY9+wSYOHlAZSD13MTbXIHUTAIVVXw286aBzMSxQzHFCW4gbFc3TYFmcD+KHR1+ZxmeeBGoT+o9SttACPIR2dU+isK/k5gC2VgJ/lsfnESrC2jPz/RGo7HDSH3rBg1gfujHngAPlpgUMuLYLG9qvLMErqMOIrxNOuCh3O7pLMLD74viG9hy2UIiVwpbz3safQXyLF6cX0K6tIis+5/Id3ebvzQAo/ljeRTNGj9loKyf2FY91GG7iiI32CAyk/P+6UEdYfpQUoSmbLSn3UD0WQ4qdGHvdrkZceClLwxNPEElTfs0a40W3pQ0U2T2AfB7IyXghGzl1hsbm1d/plOGRv/HZHEZTCkxG86tPxz+2uoziUDkBgJdVSjHSjPkNoRaRT/U/lkUmkyjXRSpU/V6BlHMeeiqlkC3bXNmP6Tcy9NH9uzEBzFvgt/Kp79RZJ86UBw2YFtLnj9l0pbicg4mKO2UTzxTEIE+pel3KBJIjPcpcRE48NAIIUjysfn5sK/zG9BDGcCu+9tEdqlwgZjqE/hJDmfBIN9vrix4lGFbi5FwWYeDCLTO/+Ulg5A4v84ZlgzKnNQ8tv76l/Tn9AOadZlMTdiNTjG6ebavdcJ0GzlmyxHZARJO5lGSpW+0YfbCrY3IfZ155QiF+N0nAPeAOtwYV5dlig1wu4ppREPVm4wk8M2DdiexqzYtKA18qCtdakQaDZg2C4U6HwYL02O1V2zeIQgSVs+CdQq3F7lUz9a0NlLVaC/Ot2NhyLYr3IxO8pqk0HDfJPmHsm+ggKDYirbacaJyDw+9tXU9HnY5h2Yx1fGXVDXkxfXqCWv7mx0+Yz7WBXbbrmWQBZHg7kqkPhPAVowDlDI2PTUvHtr5/SBG+NhNw5iaD2UMJ96DoOYg1pyHM755v/ibvd5pVOsy6A/SyT0ilpnNwD+svIhy582s4txBW4PUzwiHyPqTCTqhwiEyfPijz0/d+hmGv4zk2XkVEW7p+yU4gaPVWPKanvA0JXq5f6nQ4lxfE87LDCx7D2N+DeXeqg2FtiIXu5Fe53pbbLfocuYAQFcLOHG/qUPi2pfr7jz2YeKZncAc5gZGlIxx13dOFnoLFE9SaanBvA0IujjjvAXJleuI31Tq/JRql64NpddT9E8fpW1w/HO5E5wwHuts5a6K+gOrb/9mtXMcxZ4qf6LeZ77PJXfoFZL0aqRqU8hdR4YsLka2dxxg6yZ1UAVZVZF95GSI96E66caVYCoLLZiwrpYQfifx0o90KaQzXgbqVLGMnjdesLiCYNNaceLH3CGVEd1XICVzBMT6JhLXMpPMKpLXBx/ChgHU9EK8YIA4PdzVAnyT+kLT/og89IT2ZCFF+cQnedvKZH73DRwKHaP0mzdX70xMwcCcCw8rGe+KDVs+c8ES8CCg+zhjxJJZpogkqtMXkQRAq5li3NHLIBlx9DaYZys7+M6eOpW4v4TkHzTRMVof7Q3hdbyCnoNE3p1mkHJ/z3wCUHjNo0frjY2CLLbBopi47zLU7Mcn0gA2csITxwwCQ0eZq/a0VjKQsbXnIVEhoXgiBZnRhukmN5FxbRMYj9xsoP1MPGNsScbAF++VREKv2DMpODV1zxDp+WLKg4ssV0tw5+RD1Xd1YksnsJv7wa/Co+7TPmxawHj8p4rE/plQMeItrMUIDtxrtNVl2uyM853dypn2YA4jAWhalSws4G3d7SAR5LzM15XbXfR0GIuRP6w0iiTaJJmNn6lnn3JdO1rCV9l+3LH4yL3H6QZNw3QDlETktpUPV3378euxuGMvBklmOLpNFGbkK0U3bgjhkXsSKG65Gal9a3MeQ8Z1mTBN4UD6uQjbCWRFPnpwQfEmlaav6SKpKqdkTkNuBZDCoBzq+9BgIHOaKtLGKDNb5JPub9rwBNEl4jEZ/oiMBO/LF1UniKwDM+X/NvFvw/KMashEm+WIRl7eMaUkGEbcSooPcrmnqXShZ/HH9T4VfVDIPGlSK4CmPZVd36v5fswtyOuLm82LnpbxxeDzLw1tM3YZT6ZBGy1/43hToGCscKHTaAWXRYGL7BHujNaY1QY7eCz1L4k7Wl7gW/T8EO7MhmquiTVnFBSDrqZ26gKSOcBNO8q1Cb4p9haNI70kcSln8OpG2fGbotRkgGUAL7Ey4fZUG1K+8d4c3aTRMSMco/Fozw+wbYEtKTQH13sbMSXFLCjPOyQ4wfLu4L296IXhRkzEYj7IytA0ejB85gQu4JCrN141ODmexAqbt4dqLAKB27FPZJTdphVQWE8QOQuQcdUg8xGCvoA2tvmLnm1cmnXJzMgfK8243eOGWN6nKffAheZt8QHYo9N2B+9VtUL117TeV7qNS6WZmYUT7quhXrbA3wY69gIqcAFk6dSlM06ZQC1sKBKCFc6J8JVHLIKtxh9CJZ+REHNSGH1dQ4OP/G2bj+s59asoHIg3ldeAuyZM5g8c3nmEt3MkohwwACzLtD+cNXcY3IhC96iJRv2yUiM1+WFK5lmCRsBJ0myi47Pasmu9y9H0kCAJEvUZfCz8JnOXEpqqzOtvAlGPjfaW/iBxOZH8xZX63fmzjyQOl19UBSfQalf00v/07HnEW6re4NdfvT/AH9QDQCeZfGqFqZTUUXB8vix/jCLn+X0wZJGvl5pB6k33GBmxJ882JKte1tr7q5kFZ/lWrbJrdiZ2FyTJtvQ0iacBURgeWDeww1ZTV2WBUooAadUCFfwKcoWUAx7TXSKhMKklRvT/1rMBWtEQ10urmGaHt1lsn1Sziq7/ZN7yxdvCJTlmoR4p5M1c7lUok7yx+cY9rhAb3MNyKU++cGicvSy8gNlTm7Ixncw3B17nf5GFp0pCuocUOOutz5DBqhH/aGjIBcvrxanYMpsSxRxlnXlvtSJHD0V1LLkWYB6LiS7HOm3zMabMuRE284Vb1wwA8PWDY981Glr+RF4IfrXJkCIy1b8zYuY/wGT1h/2HMtmC/ulyRFCZV0bBrZ0iHG/c2U5lwqsRnBzE+wSVAmoxkEDrlABag4QBYXydhIOVjUwmPAyNlaxjknj7xBVO/klx/KYv/rf1V2xLqrQmMs0SC1TB3L5uFv1IbW8GyqJJS4asVQnoP+/fY4TyFXfgoFJQPB3ePcxYWzXeKgorSBOOgpS8W3j4oUhn4kO3r4tuco7Fd31vfUMBKcYQCg8Crput5EtUAdWWG2vW3V/Py6z97Elq5Sig38Tjupt8IbJS6SAAj7EQVA5K/i5snFF5ZCQNGMtJZFONHfcjkt1uiyzlZWB1GGBwzUrUekWbdsWTpjJqcAVfaPj5QrWD1MZQyGSe6ZPbLD+Yl+MYHq/zwAM7+pkl4bXZ+X2DyNNk4g9Z5y4+t03nVHQiLpZL35kK+UwpvlhzcWWJAo5RtixRuMx8O8gw+0yJ9jC+lOpG3jq4jnlYTZg1ybQDU+MILsoLp4hskmRc5L7uzCUryg/e7JDkrgUgV5+BNypC9amC77RH9Y3C76Yg1MiAz5BdHcaVsicvauGxGfjpn3NMzsQlg+NXPxSqnMKKmuth557L80mH8kEXdVaxM6RzFnNJlya69Zge8tFly67a+Ahqiy2iHBtwhHT27n7XQwb2iw9qGBwfwU/x6C9JkwaWRyX8tetaV3+mwzaHtd5N75Q0Svd3unfBhR1EIOW6+E1z3Ra7T+WEmyA89DUgDWnr9PM5Tf6k+mBMAPbb87dGo5mXDD52H6k374S7YSg77lIF2zyDlsjxowJIAMHLNOxM5ZycdgivaAN4ID6iSwMnjP5IFizwyEBQGAtkr1u8+29QvE15LvADzzKN/CZYFQoYPKqKdgAmcpYGxmLVIAJVtyna2rg8WOpBZWDujnSmA64ZXJAM/hvCUgHmQD3AYSrCUtmnAeupPaX4HZpwFJW27aXELmi73/YE5/AD0b1RvMO1suU07h8Oxxt/cjnxhmRqcWlOdBe+eN+C7ywwKJfSrFzYZ6/Lv9qbufDEt9tTrZQ/xsIvT1k01HkzbjEVP9W2zTjnmT7yNQHzH8drpDbbixegr2LhE+STQo2FoOjh5xneDOhYWQa0zatCMZ5HeVNsUEddA4fQFstOSLocjkf+DatA"
console.log(b(data))

// t 是请求对应的 payload 字典
function getSign(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    // var n = r["d"] + l(t);
    var n = "3637CB36B2E54A72A7002978D0506CDF" + l(t);
    return CryptoJS.MD5(n).toString().toLocaleLowerCase()
}

function l(t) {
    for (var e = Object.keys(t).sort(u), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]] instanceof Object || t[e[a]] instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}

function u(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}

// console.log(d({
//     "ts": 1678891184105,
//     "type": "fujian_region"
// }))