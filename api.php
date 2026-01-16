<?php
include "database.php";

$action = isset($_GET['action']) ? $_GET['action'] : '';

if($action == "create"){
    $stmt = $conn->prepare("INSERT INTO crud (name,email) VALUES (?, ?)");
    $stmt->bind_param("ss", $_POST['name'], $_POST['email']);
    $stmt->execute();
}

if($action == "read"){
    $result = $conn->query("SELECT * FROM crud");
    $data = $result->fetch_all(MYSQLI_ASSOC);
    header('Content-Type: application/json');
    echo json_encode($data);
    exit;
}

if($action == "delete"){
    $stmt = $conn->prepare("DELETE FROM crud WHERE id=?");
    $stmt->bind_param("i", $_POST['id']);
    $stmt->execute();
}

if($action == "update"){
    $stmt = $conn->prepare("UPDATE crud SET name=?, email=? WHERE id=?");
    $stmt->bind_param("ssi", $_POST['name'], $_POST['email'], $_POST['id']);
    $stmt->execute();
}
?>
