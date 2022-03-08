swaggerA:
	swagger-codegen generate --api-package AdminApi --model-package AdminModel -i /Users/zhangmingwei/Projects/Swagger/admin.json -l python -o /Users/zhangmingwei/Projects/Swagger/Admin
swaggerS:
	swagger-codegen generate --api-package ServiceApi --model-package ServiceModel -i /Users/zhangmingwei/Projects/Swagger/service.json -l python -o /Users/zhangmingwei/Projects/Swagger/Service
	