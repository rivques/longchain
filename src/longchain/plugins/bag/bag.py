try:
    import grpc
except ImportError:
    raise ImportError("The `bag` plugin is not available when the `bag` extra is not installed.")
from typing import Optional
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer as RCFContainer
from longchain.plugins.bag.api import bag_pb2_grpc, bag_pb2

class BagManager:
    app_id = None
    key = None
    owner_id = None
    base_url = None
    channel = None
    stub = None

    def configure(self, app_id: int, key: str, owner_id: str, base_url="bag-7oiuqlq3ba-uk.a.run.app:443"):
        self.app_id = app_id
        self.key = key
        self.owner_id = owner_id
        self.base_url = base_url
        self.channel = grpc.secure_channel(self.base_url, grpc.ssl_channel_credentials())
        self.stub = bag_pb2_grpc.BagServiceStub(self.channel)

        keyresult = self.stub.VerifyKey(bag_pb2.VerifyKeyRequest(appId=self.app_id, key=self.key))
        if not keyresult.valid:
            raise ValueError("Invalid Bag key. Check that your app id and key are correct.")
    
    def get_inventory(self, identity_id: str) -> bag_pb2.GetInventoryResponse:
        if self.stub is None:
            raise ValueError("BagManager not configured. Call bm_instance.configure() first.")
        result: bag_pb2.GetInventoryResponse = self.stub.GetInventory(bag_pb2.GetInventoryRequest(appId=self.app_id, key=self.key, identityId=identity_id))
        return result
    
    def create_instance(self, identity_id: str, item_id: str, quantity: int,  metadata: str = "{}", public: bool = True, show: bool = True, note: str = "") -> bag_pb2.CreateInstanceResponse:
        if self.stub is None:
            raise ValueError("BagManager not configured. Call bm_instance.configure() first.")
        result: bag_pb2.CreateInstanceResponse = self.stub.CreateInstance(bag_pb2.CreateInstanceRequest(appId=self.app_id, key=self.key, identityId=identity_id, itemId=item_id, quantity=quantity, metadata=metadata, public=public, show=show, note=note))
        return result
    
    def make_offer(self, target_identity_id: str, offer_to_give: RCFContainer[bag_pb2.OfferItem], offer_to_receive: RCFContainer[bag_pb2.OfferItem], callback_url: Optional[str] = None, slack_id_to_dm: Optional[str] = None) -> bag_pb2.MakeOfferResponse:
        if self.stub is None:
            raise ValueError("BagManager not configured. Call bm_instance.configure() first.")
        result = self.stub.MakeOffer(bag_pb2.MakeOfferRequest(appId=self.app_id, key=self.key, sourceIdentityId=self.owner_id, targetIdentityId=target_identity_id, offerToGive=offer_to_give, offerToReceive=offer_to_receive, callbackUrl=callback_url, slackIdToDm=slack_id_to_dm))
        return result
bag_instance = BagManager()

