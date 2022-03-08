# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  订单ID | 
**order_total** | **str** |  订单最终价格 订单总收入 &#x3D; Merchandise Subtotal + Shipping Fee + Order Discount + 商家改价 | 
**status** | **str** |  订单状态 待付款:Unpaid,待发货:To Ship,已发货:Shipped,已完成:Completed,已取消:Cancelled | 
**merchandise_subtotal** | **str** |  所有商品总价 | 
**shipping_fee** | **str** |  物流运费 | 
**order_discount** | **str** |  订单折扣金额 | 
**message** | **str** |  订单备注信息 | 
**create_time** | **str** |  下单时间 | 
**payment_time** | **str** |  付款时间 | 
**delivery_time** | **str** |  发货时间 | 
**completed_time** | **str** |  完成时间 | 
**cancelled_time** | **str** |  取消时间, 客户主动通过客户端取消订单, 订单付款超时 | 
**products** | [**list[OrderProduct]**](OrderProduct.md) |  订单所有商品集合 | 
**customer** | [**Customer**](Customer.md) |  | 
**note** | **str** |  工作人员处理过程中为该订单添加备注信息 | 
**order_histroy** | [**list[OrderHistory]**](OrderHistory.md) |  记录订单的处理过程，每一次的状态变更将记录一次 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

