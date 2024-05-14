# location-service
Chắc chắn rồi! Dưới đây là các ví dụ về các yêu cầu và phản hồi mẫu mà dịch vụ Định vị (Location Service) nên xử lý trong bối cảnh dịch vụ gọi xe.

### 1. Cập Nhật Vị Trí Tài Xế

**Yêu cầu**: Một tài xế gửi vị trí hiện tại của họ tới dịch vụ Định vị.

**API Endpoint**: `POST /location/update`

**Nội Dung Yêu Cầu**:
```json
{
  "driver_id": "driver123",
  "latitude": 37.7749,
  "longitude": -122.4194,
  "timestamp": "2024-05-14T08:00:00Z"
}
```

**Phản Hồi**:
```json
{
  "status": "success",
  "message": "Cập nhật vị trí thành công."
}
```

### 2. Lấy Danh Sách Tài Xế Gần Đó

**Yêu cầu**: Một hành khách yêu cầu danh sách các tài xế gần đó.

**API Endpoint**: `GET /location/nearby`

**Tham Số Yêu Cầu**:
- `latitude`: Vĩ độ của vị trí hiện tại của hành khách.
- `longitude`: Kinh độ của vị trí hiện tại của hành khách.
- `radius`: Bán kính tính bằng km để tìm kiếm các tài xế gần đó.

**URL Yêu Cầu**:
```
GET /location/nearby?latitude=37.7749&longitude=-122.4194&radius=5
```

**Phản Hồi**:
```json
{
  "status": "success",
  "drivers": [
    {
      "driver_id": "driver123",
      "latitude": 37.7750,
      "longitude": -122.4189,
      "distance_km": 0.2
    },
    {
      "driver_id": "driver456",
      "latitude": 37.7745,
      "longitude": -122.4201,
      "distance_km": 0.3
    }
  ]
}
```

### 3. Ghi Hàng Loạt Vị Trí Vào Lịch Sử Chuyến Đi

**Yêu cầu**: Ghi hàng loạt các bản cập nhật vị trí vào bảng lịch sử chuyến đi.

**API Endpoint**: `POST /location/batch`

**Nội Dung Yêu Cầu**:
```json
{
  "locations": [
    {
      "driver_id": "driver123",
      "latitude": 37.7749,
      "longitude": -122.4194,
      "timestamp": "2024-05-14T08:00:00Z"
    },
    {
      "driver_id": "driver456",
      "latitude": 37.7750,
      "longitude": -122.4189,
      "timestamp": "2024-05-14T08:01:00Z"
    }
  ]
}
```

**Phản Hồi**:
```json
{
  "status": "success",
  "message": "Ghi hàng loạt vị trí thành công."
}
```

### 4. Lấy Lịch Sử Vị Trí Chi Tiết Cho Một Chuyến Đi

**Yêu cầu**: Lấy lịch sử vị trí chi tiết cho một chuyến đi cụ thể.

**API Endpoint**: `GET /location/history`

**Tham Số Yêu Cầu**:
- `trip_id`: Mã định danh duy nhất của chuyến đi.

**URL Yêu Cầu**:
```
GET /location/history?trip_id=trip789
```

**Phản Hồi**:
```json
{
  "status": "success",
  "trip_id": "trip789",
  "locations": [
    {
      "latitude": 37.7749,
      "longitude": -122.4194,
      "timestamp": "2024-05-14T08:00:00Z"
    },
    {
      "latitude": 37.7750,
      "longitude": -122.4189,
      "timestamp": "2024-05-14T08:01:00Z"
    }
  ]
}
```

Các yêu cầu và phản hồi mẫu này thể hiện các tương tác điển hình mà dịch vụ Định vị sẽ xử lý, bao gồm cập nhật vị trí tài xế, lấy danh sách tài xế gần đó cho hành khách, ghi hàng loạt các bản cập nhật vị trí và lấy lịch sử vị trí chi tiết cho các chuyến đi.
