<?php

class NightsWatch implements IFighter {

    private $NightsWatch = array();
    public function recruit($var) {
        $this->NightsWatch[] = $var;
    }

    function fight() {
        foreach ($this->NightsWatch as $var) {
            if (method_exists(get_class($var), 'fight')) {
                $var->fight();
            }
        }
    }
}
?>

