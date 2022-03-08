# ListProductsReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  当前页码 | 
**page_size** | **int** |  展示数量 默认15 | [optional] [default to 15]
**orderby** | **str** |  排序字段(支持:created_at|price|stock|sold_out),默认 created_at | [optional] [default to 'created_at']
**sort** | **str** |  排序方式(asc,desc), 默认 desc | [optional] [default to 'desc']
**state** | **str** |  状态  all:全部, on:上架 , active:下架 , out:售罄 ,  inactive: 删除默认 all | [optional] [default to 'all']
**search** | **str** |  用户名模糊搜索 | [optional] 
**group_id** | **list[str]** |  商品分组ID搜索 | [optional] 
**category_id** | **list[str]** |  商品分类ID搜索 | [optional] 
**sold_out** | **str** |  商品起始销量搜索 | [optional] 
**price** | **str** |  商品起始价格搜索 | [optional] 
**created_at_start** | **str** |  商品创建时间起始时间 | [optional] 
**created_at_end** | **str** |  商品创建时间结束时间 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

