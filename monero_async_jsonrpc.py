from httpx import AsyncClient

class monero_async_client:
    def __init__(self, ip='127.0.0.1', port=28088, ssl_verify=False, http2=False, headers=None, proxies=None, json_id='0', jsonrpc='2.0'):
        if headers:
            self.headers = headers
        else:
            self.headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        
        self.client = AsyncClient(
            headers=self.headers,
            http2=http2,
            verify=ssl_verify,
            proxies=proxies,
        )

        self.base_json_payload = {
            'jsonrpc': jsonrpc,
            'id': json_id,
        }
        
        self.base_url = f'http://{ip}:{port}/json_rpc'
        
    async def incoming_transactions(self, **kwargs):
        get_incoming_transactions_json_payload = self.base_json_payload
        
        get_incoming_transactions_json_payload.update({
            'method': 'incoming_transfers',
        })
        
        if kwargs:
            get_incoming_transactions_json_payload.update(kwargs)
            
        get_incoming_transactions_response = await self.client.post(
            url=self.base_url, 
            json=get_incoming_transactions_json_payload
        )
        
        return get_incoming_transactions_response.json()
    
    async def get_height(self, **kwargs):
        get_height_json_payload = self.base_json_payload
        
        get_height_json_payload.update({
            'method': 'get_height',
        })
        
        if kwargs:
            get_height_json_payload.update(kwargs)
            
        get_height_response = await self.client.post(
            url=self.base_url, 
            json=get_height_json_payload
        )
        
        return get_height_response.json()
    
    async def transfer(self, **kwargs):
        transfer_json_payload = self.base_json_payload
        
        transfer_json_payload.update({
            'method': 'transfer',
        })
        
        if kwargs:
            transfer_json_payload.update(kwargs)
            
        transfer_response = await self.client.post(
            url=self.base_url, 
            json=transfer_json_payload
        )
        
        return transfer_response.json()
    
    async def get_transfers(self, **kwargs):
        get_transfer_json_payload = self.base_json_payload
        
        get_transfer_json_payload.update({
            'method': 'get_transfers',
        })
        
        if kwargs:
            get_transfer_json_payload.update(kwargs)
            
        get_transfer_response = await self.client.post(
            url=self.base_url, 
            json=get_transfer_json_payload
        )
        
        return get_transfer_response.json()
    

    async def get_balance(self, **kwargs):
        get_balance_json_payload = self.base_json_payload
        
        get_balance_json_payload.update({
            'method': 'get_balance',
        })
        
        if kwargs:
            get_balance_json_payload.update(kwargs)
            
        get_balance_response = await self.client.post(
            url=self.base_url, 
            json=get_balance_json_payload
        )
        
        return get_balance_response.json()
        
    async def make_integrated_address(self, **kwargs):
        make_integrated_address_json_payload = self.base_json_payload
        
        make_integrated_address_json_payload.update({
            'method': 'make_integrated_address',
        })
        
        if kwargs:
            make_integrated_address_json_payload.update(kwargs)
        
        make_integrated_address_response = await self.client.post(
            url=self.base_url, 
            json=make_integrated_address_json_payload
        )
        
        return make_integrated_address_response.json()
    
    async def set_daemon(self, **kwargs):
        set_daemon_json_payload = self.base_json_payload
        
        set_daemon_json_payload.update({
            'method': 'set_daemon',
        })
        
        if kwargs:
            set_daemon_json_payload.update(kwargs)
        
        set_daemon_response = await self.client.post(
            url=self.base_url, 
            json=set_daemon_json_payload
        )
        
        return set_daemon_response.json()
    
    async def rescan_blockchain(self, **kwargs):
        rescan_blockchain_json_payload = self.base_json_payload
        
        rescan_blockchain_json_payload.update({
            'method': 'rescan_blockchain',
        })
        
        if kwargs:
            rescan_blockchain_json_payload.update(kwargs)
        
        rescan_blockchain_response = await self.client.post(
            url=self.base_url, 
            json=rescan_blockchain_json_payload
        )
        
        return rescan_blockchain_response.json()
    
    async def get_payments(self, **kwargs):
        get_payments_json_payload = self.base_json_payload
        
        get_payments_json_payload.update({
            'method': 'get_payments',
        })
        
        if kwargs:
            get_payments_json_payload.update(kwargs)
        
        get_payments_response = await self.client.post(
            url=self.base_url, 
            json=get_payments_json_payload
        )
        
        return get_payments_response.json()
    
    async def get_bulk_payments(self, **kwargs):
        get_bulk_payments_json_payload = self.base_json_payload
        
        get_bulk_payments_json_payload.update({
            'method': 'get_bulk_payments',
        })
        
        if kwargs:
            get_bulk_payments_json_payload.update(kwargs)
        
        get_bulk_payments_response = await self.client.post(
            url=self.base_url, 
            json=get_bulk_payments_json_payload
        )
        
        return get_bulk_payments_response.json()