from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class App(_message.Message):
    __slots__ = ("id", "name", "description", "permissions", "public", "metadata")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    permissions: str
    public: bool
    metadata: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[str] = ..., public: bool = ..., metadata: _Optional[str] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("name", "image", "description", "reaction", "commodity", "tradable", "public", "metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    COMMODITY_FIELD_NUMBER: _ClassVar[int]
    TRADABLE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    image: str
    description: str
    reaction: str
    commodity: bool
    tradable: bool
    public: bool
    metadata: str
    def __init__(self, name: _Optional[str] = ..., image: _Optional[str] = ..., description: _Optional[str] = ..., reaction: _Optional[str] = ..., commodity: bool = ..., tradable: bool = ..., public: bool = ..., metadata: _Optional[str] = ...) -> None: ...

class Skill(_message.Message):
    __slots__ = ("name", "maxLevel", "description", "reaction", "metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAXLEVEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    maxLevel: int
    description: str
    reaction: str
    metadata: str
    def __init__(self, name: _Optional[str] = ..., maxLevel: _Optional[int] = ..., description: _Optional[str] = ..., reaction: _Optional[str] = ..., metadata: _Optional[str] = ...) -> None: ...

class Identity(_message.Message):
    __slots__ = ("slack", "inventory", "metadata")
    SLACK_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    slack: str
    inventory: _containers.RepeatedCompositeFieldContainer[Instance]
    metadata: str
    def __init__(self, slack: _Optional[str] = ..., inventory: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ..., metadata: _Optional[str] = ...) -> None: ...

class Instance(_message.Message):
    __slots__ = ("id", "itemId", "identityId", "quantity", "metadata", "item")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    id: int
    itemId: str
    identityId: str
    quantity: int
    metadata: str
    item: Item
    def __init__(self, id: _Optional[int] = ..., itemId: _Optional[str] = ..., identityId: _Optional[str] = ..., quantity: _Optional[int] = ..., metadata: _Optional[str] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class SkillInstance(_message.Message):
    __slots__ = ("id", "skillId", "identityId", "level", "metadata", "skill")
    ID_FIELD_NUMBER: _ClassVar[int]
    SKILLID_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    id: int
    skillId: str
    identityId: str
    level: int
    metadata: str
    skill: Skill
    def __init__(self, id: _Optional[int] = ..., skillId: _Optional[str] = ..., identityId: _Optional[str] = ..., level: _Optional[int] = ..., metadata: _Optional[str] = ..., skill: _Optional[_Union[Skill, _Mapping]] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ("id", "initiatorIdentityId", "receiverIdentityId", "initiatorTrades", "receiverTrades", "public", "closed")
    ID_FIELD_NUMBER: _ClassVar[int]
    INITIATORIDENTITYID_FIELD_NUMBER: _ClassVar[int]
    RECEIVERIDENTITYID_FIELD_NUMBER: _ClassVar[int]
    INITIATORTRADES_FIELD_NUMBER: _ClassVar[int]
    RECEIVERTRADES_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    CLOSED_FIELD_NUMBER: _ClassVar[int]
    id: int
    initiatorIdentityId: str
    receiverIdentityId: str
    initiatorTrades: _containers.RepeatedCompositeFieldContainer[TradeInstance]
    receiverTrades: _containers.RepeatedCompositeFieldContainer[TradeInstance]
    public: bool
    closed: bool
    def __init__(self, id: _Optional[int] = ..., initiatorIdentityId: _Optional[str] = ..., receiverIdentityId: _Optional[str] = ..., initiatorTrades: _Optional[_Iterable[_Union[TradeInstance, _Mapping]]] = ..., receiverTrades: _Optional[_Iterable[_Union[TradeInstance, _Mapping]]] = ..., public: bool = ..., closed: bool = ...) -> None: ...

class TradeInstance(_message.Message):
    __slots__ = ("id", "instanceId", "instance", "quantity")
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    id: int
    instanceId: int
    instance: Instance
    quantity: int
    def __init__(self, id: _Optional[int] = ..., instanceId: _Optional[int] = ..., instance: _Optional[_Union[Instance, _Mapping]] = ..., quantity: _Optional[int] = ...) -> None: ...

class RecipeItem(_message.Message):
    __slots__ = ("id", "recipeItemId", "recipeItem", "quantity")
    ID_FIELD_NUMBER: _ClassVar[int]
    RECIPEITEMID_FIELD_NUMBER: _ClassVar[int]
    RECIPEITEM_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    id: int
    recipeItemId: str
    recipeItem: Item
    quantity: int
    def __init__(self, id: _Optional[int] = ..., recipeItemId: _Optional[str] = ..., recipeItem: _Optional[_Union[Item, _Mapping]] = ..., quantity: _Optional[int] = ...) -> None: ...

class Recipe(_message.Message):
    __slots__ = ("id", "inputs", "outputs", "tools", "skills", "public", "description", "time")
    ID_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    inputs: _containers.RepeatedCompositeFieldContainer[RecipeItem]
    outputs: _containers.RepeatedCompositeFieldContainer[RecipeItem]
    tools: _containers.RepeatedCompositeFieldContainer[RecipeItem]
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    public: bool
    description: str
    time: int
    def __init__(self, id: _Optional[int] = ..., inputs: _Optional[_Iterable[_Union[RecipeItem, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[RecipeItem, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[RecipeItem, _Mapping]]] = ..., skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ..., public: bool = ..., description: _Optional[str] = ..., time: _Optional[int] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ("id", "locations", "tools", "branch")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    id: int
    locations: _containers.RepeatedScalarFieldContainer[str]
    tools: _containers.RepeatedScalarFieldContainer[str]
    branch: str
    def __init__(self, id: _Optional[int] = ..., locations: _Optional[_Iterable[str]] = ..., tools: _Optional[_Iterable[str]] = ..., branch: _Optional[str] = ...) -> None: ...

class ActionInstance(_message.Message):
    __slots__ = ("id", "done", "identityId", "identity", "actionId", "action")
    ID_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    ACTIONID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    done: bool
    identityId: str
    identity: Identity
    actionId: int
    action: Action
    def __init__(self, id: _Optional[int] = ..., done: bool = ..., identityId: _Optional[str] = ..., identity: _Optional[_Union[Identity, _Mapping]] = ..., actionId: _Optional[int] = ..., action: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...

class OfferItem(_message.Message):
    __slots__ = ("itemName", "quantity")
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    itemName: str
    quantity: int
    def __init__(self, itemName: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class CreateInstancesRequest(_message.Message):
    __slots__ = ("appId", "key", "instances", "identityId", "show", "note")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    identityId: str
    show: bool
    note: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., instances: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ..., identityId: _Optional[str] = ..., show: bool = ..., note: _Optional[str] = ...) -> None: ...

class CreateInstancesResponse(_message.Message):
    __slots__ = ("response", "instances")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    response: str
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    def __init__(self, response: _Optional[str] = ..., instances: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ...) -> None: ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ("appId", "key", "itemId", "identityId", "quantity", "metadata", "public", "show", "note")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    itemId: str
    identityId: str
    quantity: int
    metadata: str
    public: bool
    show: bool
    note: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., itemId: _Optional[str] = ..., identityId: _Optional[str] = ..., quantity: _Optional[int] = ..., metadata: _Optional[str] = ..., public: bool = ..., show: bool = ..., note: _Optional[str] = ...) -> None: ...

class CreateInstanceResponse(_message.Message):
    __slots__ = ("response", "instance")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    response: str
    instance: Instance
    def __init__(self, response: _Optional[str] = ..., instance: _Optional[_Union[Instance, _Mapping]] = ...) -> None: ...

class CreateAppRequest(_message.Message):
    __slots__ = ("appId", "key", "name", "description", "permissions", "public", "metadata")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    name: str
    description: str
    permissions: int
    public: bool
    metadata: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[int] = ..., public: bool = ..., metadata: _Optional[str] = ...) -> None: ...

class CreateAppResponse(_message.Message):
    __slots__ = ("response", "app", "key")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    response: str
    app: App
    key: str
    def __init__(self, response: _Optional[str] = ..., app: _Optional[_Union[App, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...

class CreateItemRequest(_message.Message):
    __slots__ = ("appId", "key", "item")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    item: Item
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class CreateItemResponse(_message.Message):
    __slots__ = ("response", "item")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    response: str
    item: Item
    def __init__(self, response: _Optional[str] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class CreateRecipeRequest(_message.Message):
    __slots__ = ("appId", "key", "recipe")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    recipe: Recipe
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., recipe: _Optional[_Union[Recipe, _Mapping]] = ...) -> None: ...

class CreateRecipeResponse(_message.Message):
    __slots__ = ("response", "recipe")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    response: str
    recipe: Recipe
    def __init__(self, response: _Optional[str] = ..., recipe: _Optional[_Union[Recipe, _Mapping]] = ...) -> None: ...

class CreateTradeRequest(_message.Message):
    __slots__ = ("appId", "key", "initiator", "receiver", "callbackUrl", "callbackMetadata", "public")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    CALLBACKURL_FIELD_NUMBER: _ClassVar[int]
    CALLBACKMETADATA_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    initiator: str
    receiver: str
    callbackUrl: str
    callbackMetadata: str
    public: bool
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., initiator: _Optional[str] = ..., receiver: _Optional[str] = ..., callbackUrl: _Optional[str] = ..., callbackMetadata: _Optional[str] = ..., public: bool = ...) -> None: ...

class CreateTradeResponse(_message.Message):
    __slots__ = ("response", "initiated")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_FIELD_NUMBER: _ClassVar[int]
    response: str
    initiated: bool
    def __init__(self, response: _Optional[str] = ..., initiated: bool = ...) -> None: ...

class CreateActionRequest(_message.Message):
    __slots__ = ("appId", "key", "action")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    action: Action
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., action: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...

class CreateActionResponse(_message.Message):
    __slots__ = ("response", "action")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    response: str
    action: Action
    def __init__(self, response: _Optional[str] = ..., action: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...

class GetIdentitiesRequest(_message.Message):
    __slots__ = ("appId", "key", "query")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    query: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...

class GetIdentitiesResponse(_message.Message):
    __slots__ = ("response", "identities")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    IDENTITIES_FIELD_NUMBER: _ClassVar[int]
    response: str
    identities: _containers.RepeatedCompositeFieldContainer[Identity]
    def __init__(self, response: _Optional[str] = ..., identities: _Optional[_Iterable[_Union[Identity, _Mapping]]] = ...) -> None: ...

class GetIdentityRequest(_message.Message):
    __slots__ = ("appId", "key", "identityId")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    identityId: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., identityId: _Optional[str] = ...) -> None: ...

class GetIdentityResponse(_message.Message):
    __slots__ = ("response", "identity")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    response: str
    identity: Identity
    def __init__(self, response: _Optional[str] = ..., identity: _Optional[_Union[Identity, _Mapping]] = ...) -> None: ...

class GetInventoryRequest(_message.Message):
    __slots__ = ("appId", "key", "identityId", "available")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    identityId: str
    available: bool
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., identityId: _Optional[str] = ..., available: bool = ...) -> None: ...

class GetInventoryResponse(_message.Message):
    __slots__ = ("response", "inventory")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    response: str
    inventory: _containers.RepeatedCompositeFieldContainer[Instance]
    def __init__(self, response: _Optional[str] = ..., inventory: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ...) -> None: ...

class GetItemRequest(_message.Message):
    __slots__ = ("appId", "key", "query")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    query: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...

class GetItemResponse(_message.Message):
    __slots__ = ("response", "item")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    response: str
    item: Item
    def __init__(self, response: _Optional[str] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class GetItemsRequest(_message.Message):
    __slots__ = ("appId", "key", "query")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    query: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...

class GetItemsResponse(_message.Message):
    __slots__ = ("response", "items")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    response: str
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, response: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class GetInstanceRequest(_message.Message):
    __slots__ = ("appId", "key", "instanceId")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    instanceId: int
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., instanceId: _Optional[int] = ...) -> None: ...

class GetInstanceResponse(_message.Message):
    __slots__ = ("response", "instance")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    response: str
    instance: Instance
    def __init__(self, response: _Optional[str] = ..., instance: _Optional[_Union[Instance, _Mapping]] = ...) -> None: ...

class GetAppRequest(_message.Message):
    __slots__ = ("appId", "key", "optAppId")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPTAPPID_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    optAppId: int
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., optAppId: _Optional[int] = ...) -> None: ...

class GetAppResponse(_message.Message):
    __slots__ = ("response", "app")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    response: str
    app: App
    def __init__(self, response: _Optional[str] = ..., app: _Optional[_Union[App, _Mapping]] = ...) -> None: ...

class GetTradeRequest(_message.Message):
    __slots__ = ("appId", "key", "query")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    query: Trade
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., query: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class GetTradeResponse(_message.Message):
    __slots__ = ("response", "trade")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRADE_FIELD_NUMBER: _ClassVar[int]
    response: str
    trade: Trade
    def __init__(self, response: _Optional[str] = ..., trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class GetTradesRequest(_message.Message):
    __slots__ = ("appId", "key", "query")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    query: Trade
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., query: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class GetTradesResponse(_message.Message):
    __slots__ = ("response", "trades")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRADES_FIELD_NUMBER: _ClassVar[int]
    response: str
    trades: _containers.RepeatedCompositeFieldContainer[Trade]
    def __init__(self, response: _Optional[str] = ..., trades: _Optional[_Iterable[_Union[Trade, _Mapping]]] = ...) -> None: ...

class GetRecipesRequest(_message.Message):
    __slots__ = ("appId", "key", "query", "inclusive")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    query: Recipe
    inclusive: bool
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., query: _Optional[_Union[Recipe, _Mapping]] = ..., inclusive: bool = ...) -> None: ...

class GetRecipesResponse(_message.Message):
    __slots__ = ("response", "recipes")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    response: str
    recipes: _containers.RepeatedCompositeFieldContainer[Recipe]
    def __init__(self, response: _Optional[str] = ..., recipes: _Optional[_Iterable[_Union[Recipe, _Mapping]]] = ...) -> None: ...

class GetRecipeRequest(_message.Message):
    __slots__ = ("appId", "key", "query")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    query: Recipe
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., query: _Optional[_Union[Recipe, _Mapping]] = ...) -> None: ...

class GetRecipeResponse(_message.Message):
    __slots__ = ("response", "recipe")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    response: str
    recipe: Recipe
    def __init__(self, response: _Optional[str] = ..., recipe: _Optional[_Union[Recipe, _Mapping]] = ...) -> None: ...

class GetActionRequest(_message.Message):
    __slots__ = ("appId", "key", "query")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    query: Action
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., query: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...

class GetActionResponse(_message.Message):
    __slots__ = ("response", "actions")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    response: str
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    def __init__(self, response: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class UpdateIdentityMetadataRequest(_message.Message):
    __slots__ = ("appId", "key", "identityId", "metadata")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    identityId: str
    metadata: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., identityId: _Optional[str] = ..., metadata: _Optional[str] = ...) -> None: ...

class UpdateIdentityMetadataResponse(_message.Message):
    __slots__ = ("response", "identity")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    response: str
    identity: Identity
    def __init__(self, response: _Optional[str] = ..., identity: _Optional[_Union[Identity, _Mapping]] = ...) -> None: ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ("appId", "key", "instanceId", "new", "show", "note")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    instanceId: int
    new: Instance
    show: bool
    note: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., instanceId: _Optional[int] = ..., new: _Optional[_Union[Instance, _Mapping]] = ..., show: bool = ..., note: _Optional[str] = ...) -> None: ...

class UpdateInstanceResponse(_message.Message):
    __slots__ = ("response", "instance")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    response: str
    instance: Instance
    def __init__(self, response: _Optional[str] = ..., instance: _Optional[_Union[Instance, _Mapping]] = ...) -> None: ...

class UpdateItemRequest(_message.Message):
    __slots__ = ("appId", "key", "itemId", "new")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    itemId: str
    new: Item
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., itemId: _Optional[str] = ..., new: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class UpdateItemResponse(_message.Message):
    __slots__ = ("response", "item")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    response: str
    item: Item
    def __init__(self, response: _Optional[str] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class UpdateAppRequest(_message.Message):
    __slots__ = ("appId", "key", "optAppId", "new")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPTAPPID_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    optAppId: int
    new: App
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., optAppId: _Optional[int] = ..., new: _Optional[_Union[App, _Mapping]] = ...) -> None: ...

class UpdateAppResponse(_message.Message):
    __slots__ = ("response", "app")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    response: str
    app: App
    def __init__(self, response: _Optional[str] = ..., app: _Optional[_Union[App, _Mapping]] = ...) -> None: ...

class UpdateTradeRequest(_message.Message):
    __slots__ = ("appId", "key", "tradeId", "identityId", "add", "remove", "callbackUrl", "callbackMetadata")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TRADEID_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    ADD_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    CALLBACKURL_FIELD_NUMBER: _ClassVar[int]
    CALLBACKMETADATA_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    tradeId: int
    identityId: str
    add: _containers.RepeatedCompositeFieldContainer[Instance]
    remove: _containers.RepeatedCompositeFieldContainer[Instance]
    callbackUrl: str
    callbackMetadata: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., tradeId: _Optional[int] = ..., identityId: _Optional[str] = ..., add: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ..., remove: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ..., callbackUrl: _Optional[str] = ..., callbackMetadata: _Optional[str] = ...) -> None: ...

class UpdateTradeResponse(_message.Message):
    __slots__ = ("response", "initiated")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_FIELD_NUMBER: _ClassVar[int]
    response: str
    initiated: bool
    def __init__(self, response: _Optional[str] = ..., initiated: bool = ...) -> None: ...

class UpdateRecipeRequest(_message.Message):
    __slots__ = ("appId", "key", "recipeId", "new")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    RECIPEID_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    recipeId: int
    new: Recipe
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., recipeId: _Optional[int] = ..., new: _Optional[_Union[Recipe, _Mapping]] = ...) -> None: ...

class UpdateRecipeResponse(_message.Message):
    __slots__ = ("response", "recipe")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    response: str
    recipe: Recipe
    def __init__(self, response: _Optional[str] = ..., recipe: _Optional[_Union[Recipe, _Mapping]] = ...) -> None: ...

class UpdateActionRequest(_message.Message):
    __slots__ = ("appId", "key", "actionId", "new")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ACTIONID_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    actionId: int
    new: Action
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., actionId: _Optional[int] = ..., new: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...

class UpdateActionResponse(_message.Message):
    __slots__ = ("response", "action")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    response: str
    action: Action
    def __init__(self, response: _Optional[str] = ..., action: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...

class DeleteAppRequest(_message.Message):
    __slots__ = ("appId", "key", "deleteAppId")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    DELETEAPPID_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    deleteAppId: int
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., deleteAppId: _Optional[int] = ...) -> None: ...

class DeleteAppResponse(_message.Message):
    __slots__ = ("response", "deletedApp")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DELETEDAPP_FIELD_NUMBER: _ClassVar[int]
    response: str
    deletedApp: App
    def __init__(self, response: _Optional[str] = ..., deletedApp: _Optional[_Union[App, _Mapping]] = ...) -> None: ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ("appId", "key", "instanceId")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    instanceId: int
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., instanceId: _Optional[int] = ...) -> None: ...

class DeleteInstanceResponse(_message.Message):
    __slots__ = ("response", "deletedInstance")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DELETEDINSTANCE_FIELD_NUMBER: _ClassVar[int]
    response: str
    deletedInstance: Instance
    def __init__(self, response: _Optional[str] = ..., deletedInstance: _Optional[_Union[Instance, _Mapping]] = ...) -> None: ...

class DeleteTradeRequest(_message.Message):
    __slots__ = ("appId", "key", "tradeId")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TRADEID_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    tradeId: int
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., tradeId: _Optional[int] = ...) -> None: ...

class DeleteTradeResponse(_message.Message):
    __slots__ = ("response", "deletedTrade")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DELETEDTRADE_FIELD_NUMBER: _ClassVar[int]
    response: str
    deletedTrade: Trade
    def __init__(self, response: _Optional[str] = ..., deletedTrade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class CloseTradeRequest(_message.Message):
    __slots__ = ("appId", "key", "tradeId", "cancel", "callbackUrl", "callbackMetadata")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TRADEID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    CALLBACKURL_FIELD_NUMBER: _ClassVar[int]
    CALLBACKMETADATA_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    tradeId: int
    cancel: bool
    callbackUrl: str
    callbackMetadata: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., tradeId: _Optional[int] = ..., cancel: bool = ..., callbackUrl: _Optional[str] = ..., callbackMetadata: _Optional[str] = ...) -> None: ...

class CloseTradeResponse(_message.Message):
    __slots__ = ("response", "initiated")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_FIELD_NUMBER: _ClassVar[int]
    response: str
    initiated: bool
    def __init__(self, response: _Optional[str] = ..., initiated: bool = ...) -> None: ...

class VerifyKeyRequest(_message.Message):
    __slots__ = ("appId", "key")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ...) -> None: ...

class VerifyKeyResponse(_message.Message):
    __slots__ = ("valid",)
    VALID_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    def __init__(self, valid: bool = ...) -> None: ...

class RunGiveRequest(_message.Message):
    __slots__ = ("appId", "key", "giverId", "receiverId", "instances")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    GIVERID_FIELD_NUMBER: _ClassVar[int]
    RECEIVERID_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    giverId: str
    receiverId: str
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., giverId: _Optional[str] = ..., receiverId: _Optional[str] = ..., instances: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ...) -> None: ...

class RunGiveResponse(_message.Message):
    __slots__ = ("response", "instances")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    response: str
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    def __init__(self, response: _Optional[str] = ..., instances: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ...) -> None: ...

class RunCraftRequest(_message.Message):
    __slots__ = ("appId", "key", "identityId", "recipeId", "callbackUrl", "callbackMetadata")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    RECIPEID_FIELD_NUMBER: _ClassVar[int]
    CALLBACKURL_FIELD_NUMBER: _ClassVar[int]
    CALLBACKMETADATA_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    identityId: str
    recipeId: int
    callbackUrl: str
    callbackMetadata: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., identityId: _Optional[str] = ..., recipeId: _Optional[int] = ..., callbackUrl: _Optional[str] = ..., callbackMetadata: _Optional[str] = ...) -> None: ...

class RunCraftResponse(_message.Message):
    __slots__ = ("response", "time")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    response: str
    time: int
    def __init__(self, response: _Optional[str] = ..., time: _Optional[int] = ...) -> None: ...

class GetCraftStatusRequest(_message.Message):
    __slots__ = ("appId", "key", "identityId")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    IDENTITYID_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    identityId: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., identityId: _Optional[str] = ...) -> None: ...

class GetCraftStatusResponse(_message.Message):
    __slots__ = ("response", "crafting")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CRAFTING_FIELD_NUMBER: _ClassVar[int]
    response: str
    crafting: bool
    def __init__(self, response: _Optional[str] = ..., crafting: bool = ...) -> None: ...

class MakeOfferRequest(_message.Message):
    __slots__ = ("appId", "key", "sourceIdentityId", "targetIdentityId", "offerToGive", "offerToReceive", "callbackUrl")
    APPID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SOURCEIDENTITYID_FIELD_NUMBER: _ClassVar[int]
    TARGETIDENTITYID_FIELD_NUMBER: _ClassVar[int]
    OFFERTOGIVE_FIELD_NUMBER: _ClassVar[int]
    OFFERTORECEIVE_FIELD_NUMBER: _ClassVar[int]
    CALLBACKURL_FIELD_NUMBER: _ClassVar[int]
    appId: int
    key: str
    sourceIdentityId: str
    targetIdentityId: str
    offerToGive: _containers.RepeatedCompositeFieldContainer[OfferItem]
    offerToReceive: _containers.RepeatedCompositeFieldContainer[OfferItem]
    callbackUrl: str
    def __init__(self, appId: _Optional[int] = ..., key: _Optional[str] = ..., sourceIdentityId: _Optional[str] = ..., targetIdentityId: _Optional[str] = ..., offerToGive: _Optional[_Iterable[_Union[OfferItem, _Mapping]]] = ..., offerToReceive: _Optional[_Iterable[_Union[OfferItem, _Mapping]]] = ..., callbackUrl: _Optional[str] = ...) -> None: ...

class MakeOfferResponse(_message.Message):
    __slots__ = ("response", "success")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    response: str
    success: bool
    def __init__(self, response: _Optional[str] = ..., success: bool = ...) -> None: ...
