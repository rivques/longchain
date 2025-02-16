# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: bag.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'bag.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tbag.proto\x12\x03\x62\x61g\"\xd1\x01\n\x03\x41pp\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0bpermissions\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x13\n\x06public\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x15\n\x08metadata\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x0e\n\x0c_descriptionB\x0e\n\x0c_permissionsB\t\n\x07_publicB\x0b\n\t_metadata\"\x9c\x02\n\x04Item\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05image\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08reaction\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x16\n\tcommodity\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x15\n\x08tradable\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x13\n\x06public\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x15\n\x08metadata\x18\x08 \x01(\tH\x07\x88\x01\x01\x42\x07\n\x05_nameB\x08\n\x06_imageB\x0e\n\x0c_descriptionB\x0b\n\t_reactionB\x0c\n\n_commodityB\x0b\n\t_tradableB\t\n\x07_publicB\x0b\n\t_metadata\"\xb9\x01\n\x05Skill\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08maxLevel\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08reaction\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x15\n\x08metadata\x18\x05 \x01(\tH\x04\x88\x01\x01\x42\x07\n\x05_nameB\x0b\n\t_maxLevelB\x0e\n\x0c_descriptionB\x0b\n\t_reactionB\x0b\n\t_metadata\"n\n\x08Identity\x12\x12\n\x05slack\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\tinventory\x18\x02 \x03(\x0b\x32\r.bag.Instance\x12\x15\n\x08metadata\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_slackB\x0b\n\t_metadata\"\xd9\x01\n\x08Instance\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06itemId\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nidentityId\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08quantity\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x15\n\x08metadata\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1c\n\x04item\x18\x06 \x01(\x0b\x32\t.bag.ItemH\x05\x88\x01\x01\x42\x05\n\x03_idB\t\n\x07_itemIdB\r\n\x0b_identityIdB\x0b\n\t_quantityB\x0b\n\t_metadataB\x07\n\x05_item\"\xdd\x01\n\rSkillInstance\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07skillId\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nidentityId\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x12\n\x05level\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x15\n\x08metadata\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1e\n\x05skill\x18\x06 \x01(\x0b\x32\n.bag.SkillH\x05\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_skillIdB\r\n\x0b_identityIdB\x08\n\x06_levelB\x0b\n\t_metadataB\x08\n\x06_skill\"\xaa\x02\n\x05Trade\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12 \n\x13initiatorIdentityId\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\x12receiverIdentityId\x18\x03 \x01(\tH\x02\x88\x01\x01\x12+\n\x0finitiatorTrades\x18\x04 \x03(\x0b\x32\x12.bag.TradeInstance\x12*\n\x0ereceiverTrades\x18\x05 \x03(\x0b\x32\x12.bag.TradeInstance\x12\x13\n\x06public\x18\x06 \x01(\x08H\x03\x88\x01\x01\x12\x13\n\x06\x63losed\x18\x07 \x01(\x08H\x04\x88\x01\x01\x42\x05\n\x03_idB\x16\n\x14_initiatorIdentityIdB\x15\n\x13_receiverIdentityIdB\t\n\x07_publicB\t\n\x07_closed\"\xa6\x01\n\rTradeInstance\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x17\n\ninstanceId\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12$\n\x08instance\x18\x03 \x01(\x0b\x32\r.bag.InstanceH\x02\x88\x01\x01\x12\x15\n\x08quantity\x18\x04 \x01(\x05H\x03\x88\x01\x01\x42\x05\n\x03_idB\r\n\x0b_instanceIdB\x0b\n\t_instanceB\x0b\n\t_quantity\"\xa7\x01\n\nRecipeItem\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x19\n\x0crecipeItemId\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\"\n\nrecipeItem\x18\x03 \x01(\x0b\x32\t.bag.ItemH\x02\x88\x01\x01\x12\x15\n\x08quantity\x18\x04 \x01(\x05H\x03\x88\x01\x01\x42\x05\n\x03_idB\x0f\n\r_recipeItemIdB\r\n\x0b_recipeItemB\x0b\n\t_quantity\"\x85\x02\n\x06Recipe\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1f\n\x06inputs\x18\x02 \x03(\x0b\x32\x0f.bag.RecipeItem\x12 \n\x07outputs\x18\x03 \x03(\x0b\x32\x0f.bag.RecipeItem\x12\x1e\n\x05tools\x18\x04 \x03(\x0b\x32\x0f.bag.RecipeItem\x12\x1a\n\x06skills\x18\x05 \x03(\x0b\x32\n.bag.Skill\x12\x13\n\x06public\x18\x06 \x01(\x08H\x01\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x07 \x01(\tH\x02\x88\x01\x01\x12\x11\n\x04time\x18\x08 \x01(\x05H\x03\x88\x01\x01\x42\x05\n\x03_idB\t\n\x07_publicB\x0e\n\x0c_descriptionB\x07\n\x05_time\"b\n\x06\x41\x63tion\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\tlocations\x18\x02 \x03(\t\x12\r\n\x05tools\x18\x03 \x03(\t\x12\x13\n\x06\x62ranch\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x05\n\x03_idB\t\n\x07_branch\"\xf0\x01\n\x0e\x41\x63tionInstance\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04\x64one\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x17\n\nidentityId\x18\x03 \x01(\tH\x02\x88\x01\x01\x12$\n\x08identity\x18\x04 \x01(\x0b\x32\r.bag.IdentityH\x03\x88\x01\x01\x12\x15\n\x08\x61\x63tionId\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12 \n\x06\x61\x63tion\x18\x06 \x01(\x0b\x32\x0b.bag.ActionH\x05\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_doneB\r\n\x0b_identityIdB\x0b\n\t_identityB\x0b\n\t_actionIdB\t\n\x07_action\"S\n\tOfferItem\x12\x15\n\x08itemName\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0b\n\t_itemNameB\x0b\n\t_quantity\"\xa2\x01\n\x16\x43reateInstancesRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12 \n\tinstances\x18\x03 \x03(\x0b\x32\r.bag.Instance\x12\x12\n\nidentityId\x18\x04 \x01(\t\x12\x11\n\x04show\x18\x05 \x01(\x08H\x00\x88\x01\x01\x12\x11\n\x04note\x18\x06 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_showB\x07\n\x05_note\"_\n\x17\x43reateInstancesResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\tinstances\x18\x02 \x03(\x0b\x32\r.bag.InstanceB\x0b\n\t_response\"\xe5\x01\n\x15\x43reateInstanceRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06itemId\x18\x03 \x01(\t\x12\x12\n\nidentityId\x18\x04 \x01(\t\x12\x10\n\x08quantity\x18\x05 \x01(\x05\x12\x15\n\x08metadata\x18\x06 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06public\x18\x07 \x01(\x08H\x01\x88\x01\x01\x12\x11\n\x04show\x18\x08 \x01(\x08H\x02\x88\x01\x01\x12\x11\n\x04note\x18\t \x01(\tH\x03\x88\x01\x01\x42\x0b\n\t_metadataB\t\n\x07_publicB\x07\n\x05_showB\x07\n\x05_note\"o\n\x16\x43reateInstanceResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12$\n\x08instance\x18\x02 \x01(\x0b\x32\r.bag.InstanceH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0b\n\t_instance\"\xd4\x01\n\x10\x43reateAppRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bpermissions\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12\x13\n\x06public\x18\x06 \x01(\x08H\x02\x88\x01\x01\x12\x15\n\x08metadata\x18\x07 \x01(\tH\x03\x88\x01\x01\x42\x0e\n\x0c_descriptionB\x0e\n\x0c_permissionsB\t\n\x07_publicB\x0b\n\t_metadata\"u\n\x11\x43reateAppResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\x03\x61pp\x18\x02 \x01(\x0b\x32\x08.bag.AppH\x01\x88\x01\x01\x12\x10\n\x03key\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x0b\n\t_responseB\x06\n\x04_appB\x06\n\x04_key\"H\n\x11\x43reateItemRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x17\n\x04item\x18\x03 \x01(\x0b\x32\t.bag.Item\"_\n\x12\x43reateItemResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x04item\x18\x02 \x01(\x0b\x32\t.bag.ItemH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x07\n\x05_item\"N\n\x13\x43reateRecipeRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x1b\n\x06recipe\x18\x03 \x01(\x0b\x32\x0b.bag.Recipe\"g\n\x14\x43reateRecipeResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\x06recipe\x18\x02 \x01(\x0b\x32\x0b.bag.RecipeH\x01\x88\x01\x01\x42\x0b\n\t_responseB\t\n\x07_recipe\"\xd3\x01\n\x12\x43reateTradeRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x11\n\tinitiator\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t\x12\x18\n\x0b\x63\x61llbackUrl\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10\x63\x61llbackMetadata\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06public\x18\x07 \x01(\x08H\x02\x88\x01\x01\x42\x0e\n\x0c_callbackUrlB\x13\n\x11_callbackMetadataB\t\n\x07_public\"_\n\x13\x43reateTradeResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tinitiated\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0c\n\n_initiated\"N\n\x13\x43reateActionRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x1b\n\x06\x61\x63tion\x18\x03 \x01(\x0b\x32\x0b.bag.Action\"g\n\x14\x43reateActionResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x0b.bag.ActionH\x01\x88\x01\x01\x42\x0b\n\t_responseB\t\n\x07_action\"A\n\x14GetIdentitiesRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\t\"^\n\x15GetIdentitiesResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12!\n\nidentities\x18\x03 \x03(\x0b\x32\r.bag.IdentityB\x0b\n\t_response\"D\n\x12GetIdentityRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\nidentityId\x18\x03 \x01(\t\"l\n\x13GetIdentityResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12$\n\x08identity\x18\x02 \x01(\x0b\x32\r.bag.IdentityH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0b\n\t_identity\"X\n\x13GetInventoryRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\nidentityId\x18\x03 \x01(\t\x12\x11\n\tavailable\x18\x04 \x01(\x08\"\\\n\x14GetInventoryResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\tinventory\x18\x02 \x03(\x0b\x32\r.bag.InstanceB\x0b\n\t_response\";\n\x0eGetItemRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\t\"N\n\x0fGetItemResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\x04item\x18\x02 \x01(\x0b\x32\t.bag.ItemB\x0b\n\t_response\"<\n\x0fGetItemsRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\t\"P\n\x10GetItemsResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x05items\x18\x02 \x03(\x0b\x32\t.bag.ItemB\x0b\n\t_response\"D\n\x12GetInstanceRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\ninstanceId\x18\x03 \x01(\x05\"l\n\x13GetInstanceResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12$\n\x08instance\x18\x02 \x01(\x0b\x32\r.bag.InstanceH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0b\n\t_instance\"=\n\rGetAppRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x10\n\x08optAppId\x18\x03 \x01(\x05\"X\n\x0eGetAppResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\x03\x61pp\x18\x02 \x01(\x0b\x32\x08.bag.AppH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x06\n\x04_app\"H\n\x0fGetTradeRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x19\n\x05query\x18\x03 \x01(\x0b\x32\n.bag.Trade\"`\n\x10GetTradeResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x05trade\x18\x02 \x01(\x0b\x32\n.bag.TradeH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x08\n\x06_trade\"I\n\x10GetTradesRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x19\n\x05query\x18\x03 \x01(\x0b\x32\n.bag.Trade\"S\n\x11GetTradesResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\x06trades\x18\x02 \x03(\x0b\x32\n.bag.TradeB\x0b\n\t_response\"q\n\x11GetRecipesRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x1a\n\x05query\x18\x03 \x01(\x0b\x32\x0b.bag.Recipe\x12\x16\n\tinclusive\x18\x04 \x01(\x08H\x00\x88\x01\x01\x42\x0c\n\n_inclusive\"V\n\x12GetRecipesResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x07recipes\x18\x02 \x03(\x0b\x32\x0b.bag.RecipeB\x0b\n\t_response\"J\n\x10GetRecipeRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x1a\n\x05query\x18\x03 \x01(\x0b\x32\x0b.bag.Recipe\"T\n\x11GetRecipeResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x06recipe\x18\x02 \x01(\x0b\x32\x0b.bag.RecipeB\x0b\n\t_response\"J\n\x10GetActionRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x1a\n\x05query\x18\x03 \x01(\x0b\x32\x0b.bag.Action\"U\n\x11GetActionResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x0b.bag.ActionB\x0b\n\t_response\"a\n\x1dUpdateIdentityMetadataRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\nidentityId\x18\x03 \x01(\t\x12\x10\n\x08metadata\x18\x04 \x01(\t\"w\n\x1eUpdateIdentityMetadataResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12$\n\x08identity\x18\x02 \x01(\x0b\x32\r.bag.IdentityH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0b\n\t_identity\"\x9b\x01\n\x15UpdateInstanceRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\ninstanceId\x18\x03 \x01(\x05\x12\x1a\n\x03new\x18\x04 \x01(\x0b\x32\r.bag.Instance\x12\x11\n\x04show\x18\x05 \x01(\x08H\x00\x88\x01\x01\x12\x11\n\x04note\x18\x06 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_showB\x07\n\x05_note\"o\n\x16UpdateInstanceResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12$\n\x08instance\x18\x02 \x01(\x0b\x32\r.bag.InstanceH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0b\n\t_instance\"W\n\x11UpdateItemRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06itemId\x18\x03 \x01(\t\x12\x16\n\x03new\x18\x04 \x01(\x0b\x32\t.bag.Item\"_\n\x12UpdateItemResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x04item\x18\x02 \x01(\x0b\x32\t.bag.ItemH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x07\n\x05_item\"i\n\x10UpdateAppRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x15\n\x08optAppId\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x15\n\x03new\x18\x04 \x01(\x0b\x32\x08.bag.AppB\x0b\n\t_optAppId\"[\n\x11UpdateAppResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\x03\x61pp\x18\x02 \x01(\x0b\x32\x08.bag.AppH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x06\n\x04_app\"\xee\x01\n\x12UpdateTradeRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07tradeId\x18\x03 \x01(\x05\x12\x12\n\nidentityId\x18\x04 \x01(\t\x12\x1a\n\x03\x61\x64\x64\x18\x05 \x03(\x0b\x32\r.bag.Instance\x12\x1d\n\x06remove\x18\x06 \x03(\x0b\x32\r.bag.Instance\x12\x18\n\x0b\x63\x61llbackUrl\x18\x07 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10\x63\x61llbackMetadata\x18\x08 \x01(\tH\x01\x88\x01\x01\x42\x0e\n\x0c_callbackUrlB\x13\n\x11_callbackMetadata\"_\n\x13UpdateTradeResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tinitiated\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0c\n\n_initiated\"]\n\x13UpdateRecipeRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x10\n\x08recipeId\x18\x03 \x01(\x05\x12\x18\n\x03new\x18\x04 \x01(\x0b\x32\x0b.bag.Recipe\"g\n\x14UpdateRecipeResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\x06recipe\x18\x02 \x01(\x0b\x32\x0b.bag.RecipeH\x01\x88\x01\x01\x42\x0b\n\t_responseB\t\n\x07_recipe\"]\n\x13UpdateActionRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x10\n\x08\x61\x63tionId\x18\x03 \x01(\x05\x12\x18\n\x03new\x18\x04 \x01(\x0b\x32\x0b.bag.Action\"g\n\x14UpdateActionResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x0b.bag.ActionH\x01\x88\x01\x01\x42\x0b\n\t_responseB\t\n\x07_action\"C\n\x10\x44\x65leteAppRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65leteAppId\x18\x03 \x01(\x05\"i\n\x11\x44\x65leteAppResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12!\n\ndeletedApp\x18\x02 \x01(\x0b\x32\x08.bag.AppH\x01\x88\x01\x01\x42\x0b\n\t_responseB\r\n\x0b_deletedApp\"G\n\x15\x44\x65leteInstanceRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\ninstanceId\x18\x03 \x01(\x05\"}\n\x16\x44\x65leteInstanceResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12+\n\x0f\x64\x65letedInstance\x18\x02 \x01(\x0b\x32\r.bag.InstanceH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x12\n\x10_deletedInstance\"A\n\x12\x44\x65leteTradeRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07tradeId\x18\x03 \x01(\x05\"q\n\x13\x44\x65leteTradeResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12%\n\x0c\x64\x65letedTrade\x18\x02 \x01(\x0b\x32\n.bag.TradeH\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0f\n\r_deletedTrade\"\xbe\x01\n\x11\x43loseTradeRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07tradeId\x18\x03 \x01(\x05\x12\x13\n\x06\x63\x61ncel\x18\x04 \x01(\x08H\x00\x88\x01\x01\x12\x18\n\x0b\x63\x61llbackUrl\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x10\x63\x61llbackMetadata\x18\x06 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_cancelB\x0e\n\x0c_callbackUrlB\x13\n\x11_callbackMetadata\"^\n\x12\x43loseTradeResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tinitiated\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0c\n\n_initiated\".\n\x10VerifyKeyRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\"\"\n\x11VerifyKeyResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\"s\n\x0eRunGiveRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07giverId\x18\x03 \x01(\t\x12\x12\n\nreceiverId\x18\x04 \x01(\t\x12 \n\tinstances\x18\x05 \x03(\x0b\x32\r.bag.Instance\"W\n\x0fRunGiveResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\tinstances\x18\x02 \x03(\x0b\x32\r.bag.InstanceB\x0b\n\t_response\"\xb1\x01\n\x0fRunCraftRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\nidentityId\x18\x03 \x01(\t\x12\x10\n\x08recipeId\x18\x04 \x01(\x05\x12\x18\n\x0b\x63\x61llbackUrl\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10\x63\x61llbackMetadata\x18\x06 \x01(\tH\x01\x88\x01\x01\x42\x0e\n\x0c_callbackUrlB\x13\n\x11_callbackMetadata\"R\n\x10RunCraftResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04time\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0b\n\t_responseB\x07\n\x05_time\"G\n\x15GetCraftStatusRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\nidentityId\x18\x03 \x01(\t\"`\n\x16GetCraftStatusResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x63rafting\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x0b\n\t_responseB\x0b\n\t_crafting\"\x83\x02\n\x10MakeOfferRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x18\n\x10sourceIdentityId\x18\x03 \x01(\t\x12\x18\n\x10targetIdentityId\x18\x04 \x01(\t\x12#\n\x0bofferToGive\x18\x05 \x03(\x0b\x32\x0e.bag.OfferItem\x12&\n\x0eofferToReceive\x18\x06 \x03(\x0b\x32\x0e.bag.OfferItem\x12\x18\n\x0b\x63\x61llbackUrl\x18\x07 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bslackIdToDm\x18\x08 \x01(\tH\x01\x88\x01\x01\x42\x0e\n\x0c_callbackUrlB\x0e\n\x0c_slackIdToDm\"H\n\x11MakeOfferResponse\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07success\x18\x02 \x01(\x08\x42\x0b\n\t_response2\xc0\x12\n\nBagService\x12<\n\tCreateApp\x12\x15.bag.CreateAppRequest\x1a\x16.bag.CreateAppResponse\"\x00\x12N\n\x0f\x43reateInstances\x12\x1b.bag.CreateInstancesRequest\x1a\x1c.bag.CreateInstancesResponse\"\x00\x12K\n\x0e\x43reateInstance\x12\x1a.bag.CreateInstanceRequest\x1a\x1b.bag.CreateInstanceResponse\"\x00\x12?\n\nCreateItem\x12\x16.bag.CreateItemRequest\x1a\x17.bag.CreateItemResponse\"\x00\x12\x45\n\x0c\x43reateRecipe\x12\x18.bag.CreateRecipeRequest\x1a\x19.bag.CreateRecipeResponse\"\x00\x12\x45\n\x0c\x43reateAction\x12\x18.bag.CreateActionRequest\x1a\x19.bag.CreateActionResponse\"\x00\x12\x42\n\x0b\x43reateTrade\x12\x17.bag.CreateTradeRequest\x1a\x18.bag.CreateTradeResponse\"\x00\x12H\n\rGetIdentities\x12\x19.bag.GetIdentitiesRequest\x1a\x1a.bag.GetIdentitiesResponse\"\x00\x12\x42\n\x0bGetIdentity\x12\x17.bag.GetIdentityRequest\x1a\x18.bag.GetIdentityResponse\"\x00\x12\x45\n\x0cGetInventory\x12\x18.bag.GetInventoryRequest\x1a\x19.bag.GetInventoryResponse\"\x00\x12\x36\n\x07GetItem\x12\x13.bag.GetItemRequest\x1a\x14.bag.GetItemResponse\"\x00\x12\x39\n\x08GetItems\x12\x14.bag.GetItemsRequest\x1a\x15.bag.GetItemsResponse\"\x00\x12\x42\n\x0bGetInstance\x12\x17.bag.GetInstanceRequest\x1a\x18.bag.GetInstanceResponse\"\x00\x12\x33\n\x06GetApp\x12\x12.bag.GetAppRequest\x1a\x13.bag.GetAppResponse\"\x00\x12\x39\n\x08GetTrade\x12\x14.bag.GetTradeRequest\x1a\x15.bag.GetTradeResponse\"\x00\x12<\n\tGetTrades\x12\x15.bag.GetTradesRequest\x1a\x16.bag.GetTradesResponse\"\x00\x12?\n\nGetRecipes\x12\x16.bag.GetRecipesRequest\x1a\x17.bag.GetRecipesResponse\"\x00\x12<\n\tGetRecipe\x12\x15.bag.GetRecipeRequest\x1a\x16.bag.GetRecipeResponse\"\x00\x12<\n\tGetAction\x12\x15.bag.GetActionRequest\x1a\x16.bag.GetActionResponse\"\x00\x12\x63\n\x16UpdateIdentityMetadata\x12\".bag.UpdateIdentityMetadataRequest\x1a#.bag.UpdateIdentityMetadataResponse\"\x00\x12K\n\x0eUpdateInstance\x12\x1a.bag.UpdateInstanceRequest\x1a\x1b.bag.UpdateInstanceResponse\"\x00\x12?\n\nUpdateItem\x12\x16.bag.UpdateItemRequest\x1a\x17.bag.UpdateItemResponse\"\x00\x12<\n\tUpdateApp\x12\x15.bag.UpdateAppRequest\x1a\x16.bag.UpdateAppResponse\"\x00\x12\x42\n\x0bUpdateTrade\x12\x17.bag.UpdateTradeRequest\x1a\x18.bag.UpdateTradeResponse\"\x00\x12\x45\n\x0cUpdateRecipe\x12\x18.bag.UpdateRecipeRequest\x1a\x19.bag.UpdateRecipeResponse\"\x00\x12\x45\n\x0cUpdateAction\x12\x18.bag.UpdateActionRequest\x1a\x19.bag.UpdateActionResponse\"\x00\x12<\n\tDeleteApp\x12\x15.bag.DeleteAppRequest\x1a\x16.bag.DeleteAppResponse\"\x00\x12K\n\x0e\x44\x65leteInstance\x12\x1a.bag.DeleteInstanceRequest\x1a\x1b.bag.DeleteInstanceResponse\"\x00\x12\x42\n\x0b\x44\x65leteTrade\x12\x17.bag.DeleteTradeRequest\x1a\x18.bag.DeleteTradeResponse\"\x00\x12?\n\nCloseTrade\x12\x16.bag.CloseTradeRequest\x1a\x17.bag.CloseTradeResponse\"\x00\x12<\n\tVerifyKey\x12\x15.bag.VerifyKeyRequest\x1a\x16.bag.VerifyKeyResponse\"\x00\x12\x36\n\x07RunGive\x12\x13.bag.RunGiveRequest\x1a\x14.bag.RunGiveResponse\"\x00\x12\x39\n\x08RunCraft\x12\x14.bag.RunCraftRequest\x1a\x15.bag.RunCraftResponse\"\x00\x12K\n\x0eGetCraftStatus\x12\x1a.bag.GetCraftStatusRequest\x1a\x1b.bag.GetCraftStatusResponse\"\x00\x12<\n\tMakeOffer\x12\x15.bag.MakeOfferRequest\x1a\x16.bag.MakeOfferResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bag_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_APP']._serialized_start=19
  _globals['_APP']._serialized_end=228
  _globals['_ITEM']._serialized_start=231
  _globals['_ITEM']._serialized_end=515
  _globals['_SKILL']._serialized_start=518
  _globals['_SKILL']._serialized_end=703
  _globals['_IDENTITY']._serialized_start=705
  _globals['_IDENTITY']._serialized_end=815
  _globals['_INSTANCE']._serialized_start=818
  _globals['_INSTANCE']._serialized_end=1035
  _globals['_SKILLINSTANCE']._serialized_start=1038
  _globals['_SKILLINSTANCE']._serialized_end=1259
  _globals['_TRADE']._serialized_start=1262
  _globals['_TRADE']._serialized_end=1560
  _globals['_TRADEINSTANCE']._serialized_start=1563
  _globals['_TRADEINSTANCE']._serialized_end=1729
  _globals['_RECIPEITEM']._serialized_start=1732
  _globals['_RECIPEITEM']._serialized_end=1899
  _globals['_RECIPE']._serialized_start=1902
  _globals['_RECIPE']._serialized_end=2163
  _globals['_ACTION']._serialized_start=2165
  _globals['_ACTION']._serialized_end=2263
  _globals['_ACTIONINSTANCE']._serialized_start=2266
  _globals['_ACTIONINSTANCE']._serialized_end=2506
  _globals['_OFFERITEM']._serialized_start=2508
  _globals['_OFFERITEM']._serialized_end=2591
  _globals['_CREATEINSTANCESREQUEST']._serialized_start=2594
  _globals['_CREATEINSTANCESREQUEST']._serialized_end=2756
  _globals['_CREATEINSTANCESRESPONSE']._serialized_start=2758
  _globals['_CREATEINSTANCESRESPONSE']._serialized_end=2853
  _globals['_CREATEINSTANCEREQUEST']._serialized_start=2856
  _globals['_CREATEINSTANCEREQUEST']._serialized_end=3085
  _globals['_CREATEINSTANCERESPONSE']._serialized_start=3087
  _globals['_CREATEINSTANCERESPONSE']._serialized_end=3198
  _globals['_CREATEAPPREQUEST']._serialized_start=3201
  _globals['_CREATEAPPREQUEST']._serialized_end=3413
  _globals['_CREATEAPPRESPONSE']._serialized_start=3415
  _globals['_CREATEAPPRESPONSE']._serialized_end=3532
  _globals['_CREATEITEMREQUEST']._serialized_start=3534
  _globals['_CREATEITEMREQUEST']._serialized_end=3606
  _globals['_CREATEITEMRESPONSE']._serialized_start=3608
  _globals['_CREATEITEMRESPONSE']._serialized_end=3703
  _globals['_CREATERECIPEREQUEST']._serialized_start=3705
  _globals['_CREATERECIPEREQUEST']._serialized_end=3783
  _globals['_CREATERECIPERESPONSE']._serialized_start=3785
  _globals['_CREATERECIPERESPONSE']._serialized_end=3888
  _globals['_CREATETRADEREQUEST']._serialized_start=3891
  _globals['_CREATETRADEREQUEST']._serialized_end=4102
  _globals['_CREATETRADERESPONSE']._serialized_start=4104
  _globals['_CREATETRADERESPONSE']._serialized_end=4199
  _globals['_CREATEACTIONREQUEST']._serialized_start=4201
  _globals['_CREATEACTIONREQUEST']._serialized_end=4279
  _globals['_CREATEACTIONRESPONSE']._serialized_start=4281
  _globals['_CREATEACTIONRESPONSE']._serialized_end=4384
  _globals['_GETIDENTITIESREQUEST']._serialized_start=4386
  _globals['_GETIDENTITIESREQUEST']._serialized_end=4451
  _globals['_GETIDENTITIESRESPONSE']._serialized_start=4453
  _globals['_GETIDENTITIESRESPONSE']._serialized_end=4547
  _globals['_GETIDENTITYREQUEST']._serialized_start=4549
  _globals['_GETIDENTITYREQUEST']._serialized_end=4617
  _globals['_GETIDENTITYRESPONSE']._serialized_start=4619
  _globals['_GETIDENTITYRESPONSE']._serialized_end=4727
  _globals['_GETINVENTORYREQUEST']._serialized_start=4729
  _globals['_GETINVENTORYREQUEST']._serialized_end=4817
  _globals['_GETINVENTORYRESPONSE']._serialized_start=4819
  _globals['_GETINVENTORYRESPONSE']._serialized_end=4911
  _globals['_GETITEMREQUEST']._serialized_start=4913
  _globals['_GETITEMREQUEST']._serialized_end=4972
  _globals['_GETITEMRESPONSE']._serialized_start=4974
  _globals['_GETITEMRESPONSE']._serialized_end=5052
  _globals['_GETITEMSREQUEST']._serialized_start=5054
  _globals['_GETITEMSREQUEST']._serialized_end=5114
  _globals['_GETITEMSRESPONSE']._serialized_start=5116
  _globals['_GETITEMSRESPONSE']._serialized_end=5196
  _globals['_GETINSTANCEREQUEST']._serialized_start=5198
  _globals['_GETINSTANCEREQUEST']._serialized_end=5266
  _globals['_GETINSTANCERESPONSE']._serialized_start=5268
  _globals['_GETINSTANCERESPONSE']._serialized_end=5376
  _globals['_GETAPPREQUEST']._serialized_start=5378
  _globals['_GETAPPREQUEST']._serialized_end=5439
  _globals['_GETAPPRESPONSE']._serialized_start=5441
  _globals['_GETAPPRESPONSE']._serialized_end=5529
  _globals['_GETTRADEREQUEST']._serialized_start=5531
  _globals['_GETTRADEREQUEST']._serialized_end=5603
  _globals['_GETTRADERESPONSE']._serialized_start=5605
  _globals['_GETTRADERESPONSE']._serialized_end=5701
  _globals['_GETTRADESREQUEST']._serialized_start=5703
  _globals['_GETTRADESREQUEST']._serialized_end=5776
  _globals['_GETTRADESRESPONSE']._serialized_start=5778
  _globals['_GETTRADESRESPONSE']._serialized_end=5861
  _globals['_GETRECIPESREQUEST']._serialized_start=5863
  _globals['_GETRECIPESREQUEST']._serialized_end=5976
  _globals['_GETRECIPESRESPONSE']._serialized_start=5978
  _globals['_GETRECIPESRESPONSE']._serialized_end=6064
  _globals['_GETRECIPEREQUEST']._serialized_start=6066
  _globals['_GETRECIPEREQUEST']._serialized_end=6140
  _globals['_GETRECIPERESPONSE']._serialized_start=6142
  _globals['_GETRECIPERESPONSE']._serialized_end=6226
  _globals['_GETACTIONREQUEST']._serialized_start=6228
  _globals['_GETACTIONREQUEST']._serialized_end=6302
  _globals['_GETACTIONRESPONSE']._serialized_start=6304
  _globals['_GETACTIONRESPONSE']._serialized_end=6389
  _globals['_UPDATEIDENTITYMETADATAREQUEST']._serialized_start=6391
  _globals['_UPDATEIDENTITYMETADATAREQUEST']._serialized_end=6488
  _globals['_UPDATEIDENTITYMETADATARESPONSE']._serialized_start=6490
  _globals['_UPDATEIDENTITYMETADATARESPONSE']._serialized_end=6609
  _globals['_UPDATEINSTANCEREQUEST']._serialized_start=6612
  _globals['_UPDATEINSTANCEREQUEST']._serialized_end=6767
  _globals['_UPDATEINSTANCERESPONSE']._serialized_start=6769
  _globals['_UPDATEINSTANCERESPONSE']._serialized_end=6880
  _globals['_UPDATEITEMREQUEST']._serialized_start=6882
  _globals['_UPDATEITEMREQUEST']._serialized_end=6969
  _globals['_UPDATEITEMRESPONSE']._serialized_start=6971
  _globals['_UPDATEITEMRESPONSE']._serialized_end=7066
  _globals['_UPDATEAPPREQUEST']._serialized_start=7068
  _globals['_UPDATEAPPREQUEST']._serialized_end=7173
  _globals['_UPDATEAPPRESPONSE']._serialized_start=7175
  _globals['_UPDATEAPPRESPONSE']._serialized_end=7266
  _globals['_UPDATETRADEREQUEST']._serialized_start=7269
  _globals['_UPDATETRADEREQUEST']._serialized_end=7507
  _globals['_UPDATETRADERESPONSE']._serialized_start=7509
  _globals['_UPDATETRADERESPONSE']._serialized_end=7604
  _globals['_UPDATERECIPEREQUEST']._serialized_start=7606
  _globals['_UPDATERECIPEREQUEST']._serialized_end=7699
  _globals['_UPDATERECIPERESPONSE']._serialized_start=7701
  _globals['_UPDATERECIPERESPONSE']._serialized_end=7804
  _globals['_UPDATEACTIONREQUEST']._serialized_start=7806
  _globals['_UPDATEACTIONREQUEST']._serialized_end=7899
  _globals['_UPDATEACTIONRESPONSE']._serialized_start=7901
  _globals['_UPDATEACTIONRESPONSE']._serialized_end=8004
  _globals['_DELETEAPPREQUEST']._serialized_start=8006
  _globals['_DELETEAPPREQUEST']._serialized_end=8073
  _globals['_DELETEAPPRESPONSE']._serialized_start=8075
  _globals['_DELETEAPPRESPONSE']._serialized_end=8180
  _globals['_DELETEINSTANCEREQUEST']._serialized_start=8182
  _globals['_DELETEINSTANCEREQUEST']._serialized_end=8253
  _globals['_DELETEINSTANCERESPONSE']._serialized_start=8255
  _globals['_DELETEINSTANCERESPONSE']._serialized_end=8380
  _globals['_DELETETRADEREQUEST']._serialized_start=8382
  _globals['_DELETETRADEREQUEST']._serialized_end=8447
  _globals['_DELETETRADERESPONSE']._serialized_start=8449
  _globals['_DELETETRADERESPONSE']._serialized_end=8562
  _globals['_CLOSETRADEREQUEST']._serialized_start=8565
  _globals['_CLOSETRADEREQUEST']._serialized_end=8755
  _globals['_CLOSETRADERESPONSE']._serialized_start=8757
  _globals['_CLOSETRADERESPONSE']._serialized_end=8851
  _globals['_VERIFYKEYREQUEST']._serialized_start=8853
  _globals['_VERIFYKEYREQUEST']._serialized_end=8899
  _globals['_VERIFYKEYRESPONSE']._serialized_start=8901
  _globals['_VERIFYKEYRESPONSE']._serialized_end=8935
  _globals['_RUNGIVEREQUEST']._serialized_start=8937
  _globals['_RUNGIVEREQUEST']._serialized_end=9052
  _globals['_RUNGIVERESPONSE']._serialized_start=9054
  _globals['_RUNGIVERESPONSE']._serialized_end=9141
  _globals['_RUNCRAFTREQUEST']._serialized_start=9144
  _globals['_RUNCRAFTREQUEST']._serialized_end=9321
  _globals['_RUNCRAFTRESPONSE']._serialized_start=9323
  _globals['_RUNCRAFTRESPONSE']._serialized_end=9405
  _globals['_GETCRAFTSTATUSREQUEST']._serialized_start=9407
  _globals['_GETCRAFTSTATUSREQUEST']._serialized_end=9478
  _globals['_GETCRAFTSTATUSRESPONSE']._serialized_start=9480
  _globals['_GETCRAFTSTATUSRESPONSE']._serialized_end=9576
  _globals['_MAKEOFFERREQUEST']._serialized_start=9579
  _globals['_MAKEOFFERREQUEST']._serialized_end=9838
  _globals['_MAKEOFFERRESPONSE']._serialized_start=9840
  _globals['_MAKEOFFERRESPONSE']._serialized_end=9912
  _globals['_BAGSERVICE']._serialized_start=9915
  _globals['_BAGSERVICE']._serialized_end=12283
# @@protoc_insertion_point(module_scope)
