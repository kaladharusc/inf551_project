angular.module('app', ["firebase"])

.controller("AppController", function($scope, $firebaseArray) {

    var ref = firebase.database().ref("dc/");
    var query = ref.orderByChild("name").limitToFirst(10);
    $scope.comics = $firebaseArray(query);

    $scope.callFireBase = function() {
        var query = ref.orderByChild("name").startAt($scope.searchInput).endAt($scope.searchInput+"\uf8ff").limitToFirst(10);
        $scope.comics = $firebaseArray(query);
    };

    $scope.callWithAlign = function() {
        if (!$scope.alignValue) {
            return;
        }
        var query = ref.orderByChild("ALIGN").equalTo($scope.alignValue).limitToFirst(10);
        $scope.comics = $firebaseArray(query);
    };

    $scope.callWithAlive = function() {
        var query = ref.orderByChild("ALIVE").equalTo($scope.aliveValue).limitToFirst(10);
        $scope.comics = $firebaseArray(query);
    };

    $scope.callWithAppearances = function() {
        var query = ref.orderByChild("APPEARANCES").startAt($scope.appearances).limitToFirst(20);
        $scope.comics = $firebaseArray(query);
    };

    $scope.callWithHair = function() {
        var query = ref.orderByChild("HAIR").equalTo($scope.hair).limitToFirst(20);
        $scope.comics = $firebaseArray(query);
    };

    $scope.callWithID = function() {
        var query = ref.orderByChild("ID").equalTo($scope.id).limitToFirst(20);
        $scope.comics = $firebaseArray(query);
    };

    $scope.callWithSex = function() {
        var query = ref.orderByChild("SEX").equalTo($scope.sex).limitToFirst(20);
        $scope.comics = $firebaseArray(query);
    };

});