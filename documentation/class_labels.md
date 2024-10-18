# Class Labels for Parking Lot Dataset

This document describes the class labels used in the parking lot dataset. The dataset consists of frames extracted from videos of outdoor parking lots, and the labels are designed to help detect different states and areas in parking scenarios.

## **Class Labels**

1. `empty_parking_space`

   **Description**:  
   This label identifies open parking spaces that are available for vehicles to park. It is used to monitor parking lot capacity and availability.  
   **Use Cases**:

   - Determining the number of available parking spots.
   - Analyzing parking lot utilization.

   **Annotation Criteria**:

   - Annotate areas clearly marked for parking but without any vehicle occupying the space.
   - Should not overlap with parked or moving vehicles.

2. `car_parked`

   **Description**:  
   This label is used to identify cars that are correctly parked within the designated parking areas.  
   **Use Cases**:

   - Tracking the number of cars parked in the lot.
   - Identifying occupancy of parking spaces.

   **Annotation Criteria**:

   - Annotate cars that are fully or mostly inside a parking spot.
   - Do not use this label for cars parked improperly or outside designated zones.

3. `obstructed_parked`

   **Description**:  
   A car that is parked but not properly within a parking space or obstructing other cars/areas.  
   **Use Cases**:

   - Detecting improper parking.
   - Identifying violations or unsafe parking behaviors.

   **Annotation Criteria**:

   - Annotate cars that are partially outside the designated parking zone or obstructing other cars.

4. `parking_zone`

   **Description**:  
   This label defines areas where parking is allowed, even if no cars are present.  
   **Use Cases**:

   - Identifying parking areas and analyzing the layout of the parking lot.
   - Understanding where parking is permitted within the lot.

   **Annotation Criteria**:

   - Mark the boundaries of parking spaces, regardless of occupancy.
   - Should align with the legal and physical layout of the parking lot.

5. `no_parking_zone`

   **Description**:  
   Areas where parking is not allowed or restricted. These may include fire lanes, exits, or loading zones.  
   **Use Cases**:

   - Monitoring illegal or unsafe parking.
   - Enforcement of parking rules and regulations.

   **Annotation Criteria**:

   - Annotate areas that are clearly marked with "No Parking" signs or similar restrictions.
   - Ensure that these areas are distinct from parking zones.

6. `car_moving`

   **Description**:  
   This label identifies cars that are in motion within the parking lot.  
   **Use Cases**:

   - Differentiating between parked and moving vehicles.
   - Analyzing traffic flow within the parking lot.

   **Annotation Criteria**:

   - Annotate cars that are visibly in motion.
   - Do not use this label for stationary cars, even if they are about to move.

## **Annotation Guidelines**

- Each frame can contain multiple labels, especially for mixed scenarios (e.g., a parking lot with both parked and moving cars).
- Be consistent with class labeling across frames and videos.
- Ensure that bounding boxes are accurate and cover the objects as closely as possible.
