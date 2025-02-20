<?php
// Enable error reporting
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Database connection file for SQLite
$database_path = "projectDB.db";

try {
    $db = new PDO("sqlite:$database_path");
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

header("Content-Type: application/json");

try {
    $stmt = $db->query("SELECT productID, productName, productDesc, price, imagePath, categoryID FROM Products");
    $products = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo json_encode($products);
} catch (PDOException $e) {
    echo json_encode(["error" => $e->getMessage()]);
}
?>