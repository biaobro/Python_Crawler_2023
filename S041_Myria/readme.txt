

"eth_accounts"

"eth_chainId"

Eip1193Fetcher

r.listAccounts();

getAddress()

listAccounts() {
                return this.send("eth_accounts", []).then((e=>e.map((e=>this.formatter.address(e)))))
            }


inpage.js

https://myria.com/airdrop/?referCode=728977
_initializeStateAsync
metamask_getProviderState

async _initializeStateAsync() {
                let e;
                try {
                    e = await this.request({
                        method: "metamask_getProviderState"
                    })
                } catch (e) {
                    this._log.error("MetaMask: Failed to get initial state. Please report this bug.", e)
                }
                this._initializeState(e)
            }