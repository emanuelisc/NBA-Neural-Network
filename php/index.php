<?php

require_once 'vendor/autoload.php';

use JasonRoman\NbaApi\Client\Client;
use JasonRoman\NbaApi\Request\Stats\Stats\Team\TeamGameLogRequest;

if (isset($_GET['teamId'])) {
    $teamId = intval($_GET['teamId']);
} else {
    $teamId = 1610612738;
}

if (isset($_GET['season'])) {
    $season = $_GET['season'];
} else {
    $season = '2015-16';
}


$client = new Client();

$request = TeamGameLogRequest::fromArray([
    'teamId'     => $teamId,
    'leagueId'   => '00',
    'season'     => $season,
    'seasonType' => 'Regular Season',
    'dateFrom'   => null,
    'dateTo'     => null,
]);

$response = $client->request($request);

$responseBody = $response->getResponseBody();
var_export($responseBody);
